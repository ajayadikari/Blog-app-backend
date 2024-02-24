from django.contrib.auth.models import BaseUserManager
from author.models import AuthorModel

class AccountManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        print(extra_fields)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        # print(user)
        return user
    
    def create_author(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        user = self.create_user(username, password, **extra_fields)
        author = AuthorModel.objects.create(account=user)
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username=username, password=password, **extra_fields)
