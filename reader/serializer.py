from rest_framework import serializers
from .models import PostModel

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"