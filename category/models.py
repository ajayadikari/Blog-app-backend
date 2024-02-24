from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False, default='unknown', unique=True)
    total_posts = models.IntegerField(null=False, default=0)
    about = models.TextField(null=False, blank=False, default="")
    