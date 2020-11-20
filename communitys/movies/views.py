from django.shortcuts import render, get_object_or_404

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieSerializer
from .models import Movie

@api_view(['GET'])
def movie_list_create(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many =True)
    return Response(serializer.data)
    