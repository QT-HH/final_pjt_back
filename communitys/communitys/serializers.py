from rest_framework import serializers
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Comment
        fields= '__all__' 
        read_only_fields = ('review',)


class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Review
        fields= ('id', 'title', 'movie_title', 'user'),


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(required=False, many=True)

    class Meta:
        model = Review
        fields = '__all__'




