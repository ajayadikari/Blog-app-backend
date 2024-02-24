from django.db import models

class AuthorModel(models.Model):
    account = models.OneToOneField('account.AccountModel', on_delete=models.CASCADE)
    total_posts = models.IntegerField(null=True, blank=True, default=0)
    total_subscribers = models.IntegerField(default=0, null=False, blank=False)
