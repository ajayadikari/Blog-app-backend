from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from account.serializer import AccountSerializer
from account.models import AccountModel
from post.models import PostModel
from .models import AuthorModel
from post.serializer import PostSerializer
from .methods import getReportedPosts
from permissions import IsAuthor, IsLoggedIn
from author.serializer import AuthorSerializer



@api_view(['POST'])
def createAuthor(request):
    data = request.data
    serialized = AccountSerializer(data=data)
    if serialized.is_valid():
        try:
            AccountModel.objects.create_author(username=serialized.validated_data.get('username'), email=serialized.validated_data.get('email'), password=serialized.validated_data.get('password'), contact=serialized.validated_data.get('contact'), bio=serialized.validated_data.get('bio'), address=serialized.validated_data.get('address'), is_author=True, first_name=serialized.validated_data.get('first_name'), last_name=serialized.validated_data.get('last_name'))
        except Exception as e:
            res = {
                "success": False,
                "message": "error creating author",
                'error': str(e)
            }
            return Response(res, status=400)
        
        res = {
                "success": True,
                "message": "author creation successful"
            }
        return Response(res)
    else:
        res = {
            "success": False,
            "message": "Error creating author",
            'error': serialized.errors
        }
        return Response(res, status=400)
    

@api_view(['GET'])
@permission_classes([IsLoggedIn, IsAuthor])
def getMyPosts(request, username=None):
    if username is not None: 
        try:
            authorIns = AccountModel.objects.get(username=username)
            author = AuthorModel.objects.get(account=authorIns)
            postsIns = PostModel.objects.filter(author=author)
            posts = PostSerializer(postsIns, many=True).data
            res = {
                "success": True, 
                "message": "your posts fetched successfully", 
                "posts": posts
            }
            return Response(res)
        except Exception as e:
            res = {
                "success": False, 
                "message": "something went wrong", 
                "error": str(e)
            }
            return Response(res, status=404)
    else:
        res = {
                "success": False, 
                "message": "your username is needed"
            }
        return Response(res, status=404)
    


@api_view(['GET'])
@permission_classes([IsLoggedIn, IsAuthor])
def getMyReported(request, username=None):
    if username is not None:
        try:
            authorIns = AccountModel.objects.get(username=username)
            author = AuthorModel.objects.get(account=authorIns)
            postsIns = PostModel.objects.filter(author=author)
            posts = PostSerializer(postsIns, many=True).data
            repPosts = getReportedPosts(posts)
            res = {
                "success": True, 
                "message": "your posts fetched successfully", 
                "posts": repPosts
            }
            return Response(res)
        except Exception as e:
            res = {
                "success": False, 
                "message": "something went wrong", 
                "error": str(e)
            }
            return Response(res, status=404)

@api_view(['GET'])
# @permission_classes([IsLoggedIn, IsAuthor])
def getAuthorStats(request, id=None):
    try:
        accountIns = AccountModel.objects.get(id=id)
        authorIns = AuthorModel.objects.get(account=accountIns)
        author = AuthorSerializer(authorIns).data
        postsIns = PostModel.objects.filter(author=authorIns).order_by('-total_likes').values('name', 'total_likes', 'id')[:5]

        res = {
            "success": True,
            "message": "Stats fetched successfully", 
            "stats": {
                "total_posts": author['total_posts'], 
                "most_liked_posts": postsIns, 
                "total_subscribers": author['total_subscribers'],
                "most_reported_posts": "feature will be available soon"
            }
        }
        return Response(res)
    except (AccountModel.DoesNotExist, AuthorModel.DoesNotExist):
        res = {
            "success": False,
            "message": "Author not found"
        }
        return Response(res, status=404)