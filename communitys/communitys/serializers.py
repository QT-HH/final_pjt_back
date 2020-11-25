from rest_framework import serializers
from .models import Review, Comment

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields=('username','password', 'MBTI')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model= Comment
        fields= ('id','content','review','user')
        read_only_fields = ('review','user')


class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model= Review
        fields= ('id', 'title', 'movie_title','user')
        read_only_fields = ('user')


class ReviewDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(required=False, many=True)
    user = UserSerializer(required=False)
    
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id','title','movie_title','rank','content')




