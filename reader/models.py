from django.db import models
from account.models import AccountModel
from author.models import AuthorModel

class ReaderModel(models.Model): 
    account = models.OneToOneField(AccountModel, on_delete=models.CASCADE)
    subscribe_limit = models.IntegerField(default=5)
    subscribed_authors = models.ManyToManyField(AuthorModel, null=True, blank=True)