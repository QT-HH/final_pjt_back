from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    overview = models.CharField(max_length=500, null=True)
    release_date = models.CharField(max_length=50)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    video = models.BooleanField()
    poster_path = models.CharField(max_length=200)
    # id = models.IntegerField(primary_key=True)
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200, null=True)
    original_language = models.CharField(max_length=50)
    original_title = models.CharField(max_length=100)
    genre_ids = models.ManyToManyField(Genre)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_movie_comments')
