from rest_framework.decorators import api_view, permission_classes
from account.models import AccountModel
from django.shortcuts import get_object_or_404
from author.models import AuthorModel
from .models import CategoryModel
from rest_framework.response import Response
from permissions import IsAuthor, IsLoggedIn
from .serializer import CategorySerializer


@api_view(['POST'])
@permission_classes([IsLoggedIn, IsAuthor])
def createCategory(request, username=None):
    if username is not None:
        account = get_object_or_404(AccountModel, username=username)
        author = get_object_or_404(AuthorModel, account=account)
        if author:
            CategoryModel.objects.create(name=request.data['name'], about=request.data['about'])
            res = {
                'success': True,
                'message': "category created"
            }
            return Response(res)
        else:
            res = {
                'success': False,
                'message': "you are not an author to create category"
            }
            return Response(res, status=404)
    else:
        res = {
                'success': False,
                'message': "author not found"
            }
        return Response(res, status=404)
    

@api_view(['GET'])
def getAllCategories(request):
    try:
        catIns = CategoryModel.objects.all()
        cat = CategorySerializer(catIns, many=True).data
        res = {
            "success": True, 
            "message": "all categories fetched", 
            "categories": cat
        }
        return Response(res)
    except Exception as e:
        res = {
            "success": False, 
            "message": "something went wrong", 
            "error": str(e)
        }
        return Response(res, status=404)