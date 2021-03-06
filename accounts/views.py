from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password2 = request.data.get('password2')

    if password != password2:
        message = {
            'error': '비밀번호가 틀립니다.'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
def getuser(request):
    # print(request.user.MBTI)
    # # serializer = UserSerializer(data=request.user)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save()
    return Response({request.user.MBTI})
