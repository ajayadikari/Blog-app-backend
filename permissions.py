from rest_framework.permissions import BasePermission
import jwt
from base.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

class IsLoggedIn(BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('Authorization').split(' ')[1]
        if token:
            try:
                decode = jwt.decode(token, SECRET_KEY, 'HS256')
                if decode:
                    user = {
                        "id": decode['user_id'],
                        "username" : decode['username'], 
                        "first_name": decode['first_name'],
                        "last_name": decode['last_name'],
                        "is_author": decode['is_author']
                    }
                    request.user = user
                    return True
                else: 
                    res = {
                        "success": False,
                        "message": "Invalid token"
                    }
                    raise PermissionDenied(detail=res)
            except jwt.ExpiredSignatureError or jwt.InvalidTokenError as e: 
                res = {
                    "success": False,
                    "message": "Authentication error", 
                    "error": str(e)
                }
                raise PermissionDenied(detail=res)
        res = {
            "success": False, 
            "message": "Token not found!"
        }
        raise PermissionDenied(detail=res)


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user:
            if user['is_author'] == True:
                return True
            else: 
                res = {
                    "success": False, 
                    "message": "Only authors are permitted"
                }
                raise PermissionDenied(detail=res)
        else:
            res = {
                    "success": False, 
                    "message": "user not found"
                }
            raise PermissionDenied(detail=res)