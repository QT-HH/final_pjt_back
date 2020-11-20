from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields=('id','title','vote_average', 'overview', 'release_date', 'popularity', 'vote_count', 'video', 'poster_path', 'adult', 'backdrop_path', 'original_language', 'original_title', 'genre_ids')