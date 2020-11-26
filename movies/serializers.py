from rest_framework import serializers
from .models import Movie, Comment

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields=('username','password', 'MBTI')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user')


class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(required=False, many=True)

    class Meta:
        model = Movie
        fields=('id','title','vote_average', 'overview', 'release_date', 'popularity', 'vote_count', 'video', 'poster_path', 'adult', 'backdrop_path', 'original_language', 'original_title', 'genre_ids', 'comments')