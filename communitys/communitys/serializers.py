from rest_framework import serializers
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Comment
        fields= ('id','content','review','user')
        read_only_fields = ('review','user')


class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Review
        fields= ('id', 'title', 'movie_title',),


class ReviewDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(required=False, many=True)
    
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id','title','movie_title','rank','content')




