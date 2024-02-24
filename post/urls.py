from django.urls import path
from .views import createPost, deletePost, getAllPostsOfAuthor, getPostById, getPostsByCategories, getPosts, getPostsByCategoryId, getFilteredPosts, getPostsBySearchTerm, updatePost, deletePost

urlpatterns = [
    path('create-post/<str:username>', createPost), 
    path('delete-post/<str:username>/<str:postid>', deletePost),
    path('getAllPostsByAuthor/<str:username>', getAllPostsOfAuthor), 
    path('getPostByid/<str:postid>', getPostById), 
    path('getPostsOfAllCategories', getPostsByCategories), 
    path('get-posts', getPosts), 
    path('get-posts-by-category-id/<str:id>', getPostsByCategoryId), 
    path('get-filtered-posts', getFilteredPosts), 
    path('get-posts-by-search-term/<str:term>', getPostsBySearchTerm), 
    path('update-post/<str:id>', updatePost),
    path('delete-post/<str:id>', deletePost)
]
