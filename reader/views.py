from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import ReaderModel
from account.models import AccountModel
from rest_framework.response import Response
from post.models import PostModel
from author.models import AuthorModel
from post.serializer import PostSerializer

@api_view(['POST'])
def createReader(request):
    data = request.data
    try:
        reader = AccountModel.objects.create_user(is_author=False, username=data['username'], contact=data['contact'], gender=data['gender'], address=data['address'], email=data['email'], password=data['password'], imageUrl=data['imageUrl'])
        ReaderModel.objects.create(account=reader)
        res = {
            "success": True, 
            "message": "profile created", 
        }
        return Response(res)
    except Exception as e:
        res = {
            "success": False, 
            "message": "error while profile creation",
            'error': str(e)
        }
        return Response(res, status=404)


@api_view(['POST'])
def likePost(request, username=None, postid=None):
    if username is not None:
        user = get_object_or_404(AccountModel, username=username)
        reader = ReaderModel.objects.get(account=user)
        post = get_object_or_404(PostModel, id=postid)
        if reader in post.likes.all():
            res = {
                "success": False,
                "message": "you already liked the post"
            }
            return Response(res, status=400)
        post.likes.add(reader)
        post.total_likes += 1
        post.save()
        res = {
            "success": True, 
            "message": "you liked post", 
        }
        return Response(res)
    else:
        res = {
            "success": False, 
            "message": "something went wrong"
        }
        return Response(res, status=404)
    

@api_view(['POST'])
def unLikePost(request, username=None, postid=None):
    if username is not None:
        user = get_object_or_404(AccountModel, username=username)
        reader = ReaderModel.objects.get(account=user)
        post = get_object_or_404(PostModel, id=postid)
        if reader not in post.likes.all():
            res = {
                "success": False,
                "message": "you never liked the post"
            }
            return Response(res, status=400)
        post.likes.remove(reader)
        post.total_likes -= 1
        post.save()
        res = {
            "success": True, 
            "message": "you unliked post", 
        }
        return Response(res)
    else:
        res = {
            "success": False, 
            "message": "something went wrong"
        }
        return Response(res, status=404)


@api_view(['POST'])
def reportPost(request, username=None, postid=None):
    if username is not None:
        user = get_object_or_404(AccountModel, username=username)
        reader = ReaderModel.objects.get(account=user)
        post = get_object_or_404(PostModel, id=postid)
        if reader in post.reports.all():
            res = {
                "success": False,
                "message": "you reported the post"
            }
            return Response(res, status=400)
        post.reports.add(reader)
        post.total_reports += 1
        post.save()
        res = {
            "success": True, 
            "message": "you report post", 
        }
        return Response(res)
    else:
        res = {
            "success": False, 
            "message": "something went wrong"
        }
        return Response(res, status=404)
    

@api_view(['POST'])
def unReportPost(request, username=None, postid=None):
    if username is not None:
        user = get_object_or_404(AccountModel, username=username)
        reader = ReaderModel.objects.get(account=user)
        post = get_object_or_404(PostModel, id=postid)
        if reader not in post.reports.all():
            res = {
                "success": False,
                "message": "you never reported the post"
            }
            return Response(res, status=400)
        post.reports.remove(reader)
        post.total_reports -= 1
        post.save()
        res = {
            "success": True, 
            "message": "report removed", 
        }
        return Response(res)
    else:
        res = {
            "success": False, 
            "message": "something went wrong"
        }
        return Response(res, status=404)


@api_view(['POST'])
def subscribeAuthor(request, readername=None, authorname=None):
    authorAcc = AccountModel.objects.get(username=authorname)
    author = AuthorModel.objects.get(account=authorAcc)
    readerIns = AccountModel.objects.get(username=readername)
    reader = ReaderModel.objects.get(account=readerIns)
    if not reader.subscribed_authors.filter(id=author.id).exists():
        if reader.subscribe_limit > 0:
            reader.subscribed_authors.add(author)
            reader.subscribe_limit -= 1
            author.total_subscribers += 1
            reader.save()
            author.save()
            
            res = {
                "success": True, 
                "message": "subscribed"
            }
            return Response(res)
        else:
            res = {
                "success": False, 
                "message": "please increase your subscription plan"
            }
            return Response(res, status=400)
    else:
        res = {
            "success": False, 
            "message": "you are already a subscriber"
        }
        return Response(res, status=404)
        
        

@api_view(['POST'])
def unSubscribeAuthor(request, readername=None, authorname=None):
    authorAcc = AccountModel.objects.get(username=authorname)
    author = AuthorModel.objects.get(account=authorAcc)
    readerIns = AccountModel.objects.get(username=readername)
    reader = ReaderModel.objects.get(account=readerIns)
    if reader.subscribed_authors.filter(id=author.id).exists():
            reader.subscribed_authors.remove(author)
            reader.subscribe_limit += 1
            author.total_subscribers -= 1
            reader.save()
            author.save()
            res = {
                "success": True, 
                "message": "unsubscribed"
            }
            return Response(res)
    else:
        res = {
            "success": False, 
            "message": "you have not subscribed"
        }
        return Response(res, status=404)
    

@api_view(['GET'])
def getLikedPosts(request, username=None):
    if username is not None:
        readerIns = AccountModel.objects.get(username=username)
        reader = ReaderModel.objects.get(account=readerIns)
        likepostsIns = PostModel.objects.filter(likes=reader)
        likedposts = PostSerializer(likepostsIns, many=True).data
        res = {
            "success": True,
            "message": "fetched blogs that you liked", 
            "likedPosts": likedposts
        }
        return Response(res)
    else:
        res = {
            "success": False,
            "message": "need your username to fetch liked posts"
        }
        return Response(res, status=404)
        
@api_view(['GET'])
def getLikedPostsIdByUserId(request, username=None):
    if username is not None:
        readerIns = AccountModel.objects.get(username=username)
        reader = ReaderModel.objects.get(account=readerIns)
        ids = PostModel.objects.filter(likes=reader).values('id')
        res = {
            "success": True,
            "message": "fetched blogs that you liked", 
            "ids": ids
        }
        return Response(res)
    else:
        res = {
            "success": False,
            "message": "need your username to fetch liked posts"
        }
        return Response(res, status=404)
    
@api_view(['GET'])
def alreadySubscribed(request, readerId=None, authorId=None):
    if readerId is not None and authorId is not None:
        readerAcc = AccountModel.objects.get(id=readerId)
        authorAcc = AccountModel.objects.get(id=authorId)
        reader = ReaderModel.objects.get(account=readerAcc)
        author = AuthorModel.objects.get(account=authorAcc)
        subscibed = author in reader.subscribed_authors.all()
        res = {
            "success": True, 
            "message": "data fetched",
            "subscribed": subscibed
        }
        return Response(res)
    else:
        res = {
            "success": False, 
            "message": "unable to fetch data"
        }
        return Response(res, status=404)