from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ReviewSerializer, CommentSerializer, ReviewListSerializer
from .models import Review, Comment


@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request):
    if request.method == 'GET':
        reviews = Review.objects.order_by('-pk')
        serializer = ReviewSerializer(reviews, many =True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ArticleSerializer(review)
    return Response(serializer.data)


@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request,movie_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'})
    
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        review.delete()
        return Response({'id': review_pk}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user= request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ArticleSerializer(review)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'})
        
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user= request.user)
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)