from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from account.models import AccountModel
from author.models import AuthorModel
from .models import PostModel
from rest_framework.response import Response
from category.models import CategoryModel
from .methods import getAllPosts, getAllPostsByCategories
from .serializer import PostSerializer
from permissions import IsLoggedIn, IsAuthor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q 
from author.serializer import AuthorSerializer

@api_view(['POST'])
@permission_classes([IsLoggedIn, IsAuthor])
def createPost(request, username=None):
    if username is not None:
        account = get_object_or_404(AccountModel, username=username)
        author = get_object_or_404(AuthorModel, account=account)
        if author:
            try:
                category = CategoryModel.objects.get(name=request.data['category'])
                post = PostModel.objects.create(author=author, category=category, name=request.data['name'], content=request.data['content'], imgUrl=request.data['imgUrl'])
                category.total_posts += 1
                author.total_posts += 1
                category.save()
                author.save()
                res = {
                    "success": True, 
                    "message": "post created!"
                }
                return Response(res)
            except Exception as e:
                print(e)
                res = {
                    "success": False, 
                    "message": "unable to create post", 
                    "error": str(e)
                }
                return Response(res, status=400)
                
        else:
            res = {
                    "success": False, 
                    "message": "something went wrong", 
                    "error": "author not found!"
                }
            return Response(res, status=400)
    

@api_view(['DELETE'])
@permission_classes([IsLoggedIn, IsAuthor])
def deletePost(request, username=None, postid=None):
    if username is not None:
        account = get_object_or_404(AccountModel, username=username)
        author = get_object_or_404(AuthorModel, account=account)
        post = PostModel.objects.get(id=postid, author=author)
        if post:
            post.delete()
        else:
            res = {
                "success": False, 
                "message": "post not found"
            }
            return Response(res, status=400)
        res = {
                "success": True, 
                "message": "post deleted successfully"
            }
        return Response(res)


@api_view(['GET'])
def getAllPostsOfAuthor(request, username=None):
    POSTS_PER_PAGE = 4
    if username is not None:
        account = get_object_or_404(AccountModel, username=username)
        author = get_object_or_404(AuthorModel, account=account)
        authorDetails = AuthorSerializer(author).data
        posts = PostModel.objects.filter(author=author).order_by('id')
        page_number = request.query_params.get('page', 1)
        post_paginator = Paginator(posts, POSTS_PER_PAGE)
        page_obj = post_paginator.get_page(int(page_number))
        serialized_posts = PostSerializer(page_obj, many=True).data
        res = {
            "success": True, 
            "message": "All posts fetched successfully", 
            "posts": serialized_posts, 
            "has_next": page_obj.has_next()
        }
        return Response(res)
    else:
        res = {
            "success": False, 
            "message": "username needed"
        }
        return Response(res, status=400)


@api_view(['GET'])
def getPostById(request, postid=None):
    if postid is not None:
        try:
            postIns = PostModel.objects.get(id=postid)
            post = PostSerializer(postIns).data
            res = {
                "success": True, 
                "message": "post fetched successfully", 
                "post": post
            }
            return Response(res)
        except Exception as e:
            res = {
                    "success": False, 
                    "message": "post does not exists",
                    "error": str(e)
                }
            return Response(res, status=404)
    else:
        res = {
                "success": False, 
                "message": "post id is needed", 
                "post": post
            }
        return Response(res, status=404)
    

@api_view(['GET'])
def getPostsByCategories(request):
    try:
        POSTS_PER_PAGE = 4
        page = request.query_params.get('page')
        categories = CategoryModel.objects.all()
        posts = getAllPostsByCategories(categories)
        post_paginator = Paginator(posts, POSTS_PER_PAGE)
        page_obj = post_paginator.get_page(page)
        posts = PostSerializer(page_obj, many=True).data
        res = {
            'success': True, 
            "message": "All posts fetched", 
            "posts": posts, 
            "has_next": page_obj.has_next()
        }
        return Response(res)
    except Exception as e:
        res = {
            'success': False, 
            "message": "something went wrong", 
            "error": str(e)
        }
        return Response(res, status=400)
    


@api_view(['GET'])
def getPosts(request):
    print(request.user)
    try:
        POSTS_PER_PAGE = 4
        page = request.query_params.get('page')
        postsIns = PostModel.objects.order_by('-created_at')
        paginator = Paginator(postsIns, POSTS_PER_PAGE)
        page_obj = paginator.get_page(page)
        posts = PostSerializer(page_obj, many=True).data
        res = {
            "success": True, 
            "message": "posts fetched successfully", 
            "posts": posts, 
            "has_next": page_obj.has_next()
        }
        return Response(res)
    except Exception as e:
        res = {
            "success": False, 
            "message": "unable to fetch posts", 
            "error": str(e)
        }
        return Response(res, status=400)
    
@api_view(['GET'])
def getPostsByCategoryId(request, id=None):
    if id is not None:
        try:
            POSTS_PER_PAGE = 4
            category = CategoryModel.objects.get(id=id)
            postsIns = PostModel.objects.filter(category=category)
            page = request.query_params.get('page')
            paginator = Paginator(postsIns, POSTS_PER_PAGE)
            page_obj = paginator.get_page(page)
            posts = PostSerializer(page_obj, many=True).data
            res = {
                "success": True, 
                "message": "All posts fetches",
                "posts": posts, 
                "has_next": page_obj.has_next()
            }
            return Response(res)
        except Exception as e:
            res = {
                "success": False, 
                "message": "unable to fetch posts",
                "error": str(e)
            }
            return Response(res, status=404)

    

@api_view(['GET'])
def getFilteredPosts(request):
    try:
        POSTS_PER_PAGE = 4
        categories = request.query_params.getlist('category')
        categoriesIns = CategoryModel.objects.filter(id__in=categories)
        postsIns = PostModel.objects.filter(category__in=categoriesIns)
        paginator = Paginator(postsIns, POSTS_PER_PAGE)
        page = request.query_params.get('page')
        page_obj = paginator.get_page(page)
        posts = PostSerializer(page_obj, many=True).data
        res = {
            "success": True, 
            "message": "All filtered posts are fetched", 
            "posts": posts, 
            "has_next": page_obj.has_next()
        }
        return Response(res)
    except Exception as e: 
        res = {
            "success": False, 
            "message": "unable to fetch posts", 
            "error": str(e)
        }
        return Response(res, status=404)
    

@api_view(['GET'])
def getPostsBySearchTerm (request, term=None):
    if term is not None:
        try:
            POST_PER_PAGE = 4
            postsIns = PostModel.objects.filter(name__icontains=term)
            page = request.query_params.get('page')
            paginator = Paginator(postsIns, POST_PER_PAGE)
            page_obj = paginator.get_page(page)
            posts = PostSerializer(page_obj, many=True).data
            res = {
                "success": True, 
                "message": "Fetches posts", 
                "posts": posts, 
                "has_next": page_obj.has_next()
            }
            return Response(res)
        except Exception as e:
            res = {
                "success": False, 
                "message": "unable to fetch posts", 
                "error": str(e)
            }
            return Response(res, status=400)
    else:
        res = {
            "success": False, 
            "message": "unable to fetch posts", 
            "error": "search term is empty"
        }
        return Response(res, status=400)


@api_view(['PATCH'])
def updatePost(request, id=None):
    if id is not None:
        data = request.data
        postIns = PostModel.objects.get(id=id)
        serialized = PostSerializer(postIns, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            res = {
            "success": True, 
            "message": "post updation successful"
            }
            return Response(res)
        else:
            res = {
            "success": False, 
            "message": "post updation failed", 
            "error": serialized.errors
        }
        return Response(res, status=400)
    else:
        res = {
            "success": False, 
            "message": "post updation failed", 
            "error": "post id is needed"
        }
        return Response(res, status=404)

@api_view(['DELETE'])
def deletePost(request, id=None):
    if id is not None:
        postIns = PostModel.objects.get(id=id)
        postAuthor = PostModel.objects.filter(id=id).values('author')[:1]
        authorIns = AuthorModel.objects.get(id=postAuthor)
        authorIns.total_posts -= 1
        authorIns.save()
        postIns.delete()
        res = {
            "success": True, 
            "message": "post deleted successfully"
        }
        return Response(res)
    else:
        res = {
            "success": False, 
            "message": "post deletion failed", 
            "error": "post id is needed"
        }
        return Response(res, status=400)