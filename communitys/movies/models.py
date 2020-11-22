from django.db import models

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
