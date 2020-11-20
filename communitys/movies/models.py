from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=50)
    pubDate = models.IntegerField()
    director = models.CharField(max_length=50)
    actor = models.CharField(max_length=200)
    userRating = models.FloatField()
