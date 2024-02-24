from rest_framework import serializers
from .models import PostModel
from reader.models import ReaderModel

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    author_id = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ['id', 'updated_at', 'created_at', 'total_reports', 'total_likes', 'category_name', 'total_likes', 'author_name', 'content', 'name', 'imgUrl', 'author_id']

    def get_category_name(self, obj):
        return obj.category.name

    def get_author_name(self, obj):
        return obj.author.account.first_name + " " + obj.author.account.last_name
    
    def get_author_id(self, obj):
        return obj.author.account.id
