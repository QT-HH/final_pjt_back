from rest_framework import serializers
from .models import Movie, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user')


class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(required=False, many=True)

    class Meta:
        model = Movie
        fields=('id','title','vote_average', 'overview', 'release_date', 'popularity', 'vote_count', 'video', 'poster_path', 'adult', 'backdrop_path', 'original_language', 'original_title', 'genre_ids', 'comments')