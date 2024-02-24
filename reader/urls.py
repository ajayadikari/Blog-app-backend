from rest_framework.urls import path
from .views import createReader, likePost, unLikePost, reportPost, unReportPost, subscribeAuthor, unSubscribeAuthor, getLikedPosts, getLikedPostsIdByUserId, alreadySubscribed


urlpatterns = [
    path('create-reader', createReader),
    path('like-post/<str:username>/<str:postid>', likePost), 
    path('unlike-post/<str:username>/<str:postid>', unLikePost), 
    path('report-post/<str:username>/<str:postid>', reportPost), 
    path('unreport-post/<str:username>/<str:postid>', unReportPost), 
    path('subscribe/<str:readername>/<str:authorname>', subscribeAuthor),
    path('unsubscribe/<str:readername>/<str:authorname>', unSubscribeAuthor),
    path('liked-posts/<str:username>', getLikedPosts), 
    path('liked-posts-id/<str:username>', getLikedPostsIdByUserId), 
    path('is-reader-subscribed/<str:readerId>/<str:authorId>', alreadySubscribed)
]
