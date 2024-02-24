from django.contrib import admin
from .models import AccountModel

class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_staff', 'is_author', 'is_superuser']

    fieldsets = [
        ("credentials", {'fields':("username", "email", "password")}), 
        ("details", {"fields": (("first_name", "last_name"), "contact", "gender", "address", "bio", "imageUrl")}), 
        ("status", {'fields': ("is_staff", "is_author", "is_superuser")}), 
        ("Permissions", {'fields': ("groups", "user_permissions")})
    ]

    search_fields = ['username', 'email', 'contact']


admin.site.register(AccountModel, AccountAdmin)