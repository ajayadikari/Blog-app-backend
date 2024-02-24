from django.contrib import admin
from .models import PostModel

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_name', 'total_likes', 'total_reports']
    list_filter = ['total_likes', 'total_reports']
    search_fields = ["name"]

    def category_name(self, obj):
        return obj.category.name


admin.site.register(PostModel, PostAdmin)