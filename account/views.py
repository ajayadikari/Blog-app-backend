from rest_framework.decorators import api_view, permission_classes
from permissions import IsLoggedIn
from django.shortcuts import get_object_or_404
from .models import AccountModel
from .serializer import AccountSerializer
from rest_framework.response import Response

@api_view(['GET'])
# @permission_classes([IsLoggedIn])
def getAccount(request, id=None):
    if id is not None:
        try:
            accountIns = AccountModel.objects.get(id=id)
            account = AccountSerializer(accountIns).data
            res = {
                "success": True, 
                "message": 'account fetch successful', 
                'account': account
            }
            return Response(res)
        except Exception as e:
            res = {
                "success": False, 
                "message": 'account fetch failed', 
                'error': str(e)
            }
            return Response(res, status=404)
    else:
        res = {
                "success": False, 
                "message": 'user id needed to fetch account'
            }
        return Response(res, status=404)
    

@api_view(['PATCH'])
@permission_classes([IsLoggedIn])
def updateProfile(request, id=None):
    if(id is not None):
        accountIns = get_object_or_404(AccountModel, id=id)
        serializer = AccountSerializer(accountIns, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {
                "success": True, 
                "message": "Profile updated successfully"
            }
            return Response(res)
        else:
            res = {
                "success": False, 
                "message": "Profile updation failed", 
                "errors": serializer._errors
            }
            return Response(res, status=400)
    else:
        res = {
                "success": False, 
                "message": "user id is needed", 
                "error": "user id is needed"
            }     
        return Response(res, status=404)
    

@api_view(['GET'])
def getUserImage(request, id=None):
    if id is not None:
        try:
            imgUrl = AccountModel.objects.filter(id=id).values('imageUrl')
            res = {
                "success": True, 
                "message": "User image is fetched", 
                "imgUrl": imgUrl
            }
            return Response(res)
        except Exception as e:
            res = {
                "success": False, 
                "message": "error occured while fetching user image url", 
                "error": str(e)
            }
            return Response(res, status=400)
    else:
        res = {
                "success": False, 
                "message": "user id is needed to get the img url", 
                "error": "user id is needed to get the img url"
            }
        return Response(res, status=400)
    

@api_view(['GET'])
def getUserIdByName(request, name=None):
    if name is not None:
        try:
            id = AccountModel.objects.filter(username=name).values('id')
            res = {
                "success": True, 
                "message": "id fetched", 
                "id": id
            }
            return Response(res)
        except Exception as e:
            res = {
                "success": False, 
                "message": "error occured", 
                "error": str(e)
            }
            return Response(res, status=400)
    else:
        res = {
            "success": False, 
            "message": "id is needed"
        }
        return Response(res, status=400)

