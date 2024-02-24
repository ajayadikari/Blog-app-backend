from django.db import models
from author.models import AuthorModel
from reader.models import ReaderModel
from category.models import CategoryModel

class PostModel(models.Model):

    report_choices = [
        ('1', 'abusive content'), 
        ('2', 'wrong information'), 
        ('3', 'irrelevant'), 
        ('4', 'misleading')
    ]
    name = models.CharField(max_length=255, null=False, blank=False, default="no title", unique=True)
    content = models.TextField(null=False, blank=False, default="")
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    likes = models.ManyToManyField(ReaderModel, related_name='liked_posts', null=True, blank=True)
    category = models.ForeignKey(CategoryModel, null=False, blank=False, default='unknown', on_delete=models.SET_DEFAULT)
    total_likes = models.IntegerField(null=False, default=0)
    reports = models.ManyToManyField(ReaderModel, related_name='reported_posts', null=True, blank=True)
    total_reports = models.IntegerField(null=False, default=0)
    report_reason = models.CharField(max_length=255, null=True, blank=True)
    imgUrl = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
