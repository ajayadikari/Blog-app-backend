from rest_framework.urls import path
from .views import createAuthor, getMyPosts, getMyReported, getAuthorStats

urlpatterns = [
    path('create-author', createAuthor), 
    path('get-my-posts/<str:username>', getMyPosts), 
    path('get-my-reported-posts/<str:username>', getMyReported), 
    path('get-stats/<str:id>', getAuthorStats)
]
