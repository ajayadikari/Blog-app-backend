from django.urls import path
from .views import getAccount, updateProfile, getUserImage, getUserIdByName

urlpatterns = [
    path('get-user-account/<str:id>', getAccount), 
    path('update-profile/<str:id>', updateProfile), 
    path('get-user-img/<str:id>', getUserImage), 
    path('get-id-by-name/<str:name>', getUserIdByName)
]
