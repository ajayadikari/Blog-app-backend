from django.contrib import admin
from .models import CategoryModel

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'total_posts']


admin.site.register(CategoryModel, CategoryAdmin)