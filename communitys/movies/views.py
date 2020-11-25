from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import MovieSerializer, CommentSerializer
from .models import Movie, Comment

from django.db.models import Q
import random


@api_view(['GET'])
def movie_list_create(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        comments = Comment.objects.filter(movie_id=movie_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user= request.user, movie= movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.my_movie_comments.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'})

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user= request.user)
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommanded_1(request):
    mbti_genres = {
        1: [28, 10749],
        2: [10752, 80],
        3: [10751, 35],
        4: [10402, 12],
        5: [53, 80],
        6: [99, 9648],
        7: [28, 18],
        8: [14, 28],
        9: [99, 10751],
        10: [878, 28],
        11: [10749, 16],
        12: [10749, 14],
        13: [878, 14],
        14: [878, 9648],
        15: [18, 36],
        16: [27, 53],
    }

    movies = Movie.objects.filter(Q(genre_ids = mbti_genres.get(request.user.MBTI)[0]) | Q(genre_ids = mbti_genres.get(request.user.MBTI)[1])).order_by('?')[:10]
    idx = random.randint(0, 9)
    movie = movies[idx]
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommanded_2(request):
    comments = Comment.objects.filter(user_id=request.user.id, rank__gte=3).order_by('?')[:10]
    # comments = Comment.objects.filter(user_id=request.user.id, rank__gte=3).order_by('?')
    
    if not comments.exists():
        return Response({'detail': '영화를 추천받으시려면 시청하신 영화에 평점을 등록해주세요.'})
    
    idx = random.randint(0, len(comments)-1)
    movie = Movie.objects.get(id = comments[idx].movie_id)
    rec_movie = Movie.objects.filter(genre_ids=movie.genre_ids.all()[0].id)
    serializer = MovieSerializer(rec_movie[0])


    return Response(serializer.data)