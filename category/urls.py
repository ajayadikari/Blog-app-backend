from rest_framework.urls import path
from .views import createCategory, getAllCategories


urlpatterns = [
    path('create-category/<str:username>', createCategory), 
    path('get-all-categories', getAllCategories)
]
