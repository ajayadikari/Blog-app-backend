from django.contrib import admin
from .models import AuthorModel


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["username", 'author_name', 'total_posts', 'total_subscribers']
    list_filter = ['total_posts']
    search_fields = ['author_name']

    def author_name(self, obj):
        return obj.account.first_name +" "+ obj.account.last_name
    
    def username(self, obj):
        return obj.account.username
    

admin.site.register(AuthorModel, AuthorAdmin)