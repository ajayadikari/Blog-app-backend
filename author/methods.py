from post.serializer import PostSerializer


def getReportedPosts(posts):
    print(posts)
    repPosts = []
    for post in posts:
        print(post)
        if post['total_reports'] > 0:
            repPosts.append(post)

    return repPosts