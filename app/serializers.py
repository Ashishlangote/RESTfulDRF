from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=100)
    
    class Meta:
        model = Post
        fields = ["title", "content", "date_posted", "author"]