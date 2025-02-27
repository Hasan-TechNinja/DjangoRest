from rest_framework import serializers
from . models import Blog, Comment




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        comment = CommentSerializer(many=True, read_only = True)
        model = Blog
        fields = "__all__"