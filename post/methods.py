from .serializer import PostSerializer
from .models import PostModel
from .serializer import PostSerializer


def getAllPosts(posts):
    allPosts = []
    for post in posts:
        allPosts.append(PostSerializer(post).data)
    return allPosts
    

def getAllPostsByCategories(categories):
    Allposts = []
    for category in categories:
        postsIns = PostModel.objects.filter(category=category)
        posts = PostSerializer(postsIns, many=True).data
        obj = {
            "category": category.name, 
            "posts": posts
        }
        
        Allposts.append(obj)
    return Allposts

