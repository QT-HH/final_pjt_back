from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mbti_choice = (
        (1, 'ESTJ'), (2, 'ESTP'), (3, 'ESFJ'), (4, 'ESFP'), 
        (5, 'ENTJ'), (6, 'ENTP'), (7, 'ENFJ'), (8, 'ENFP'), 
        (9, 'ISTJ'), (10, 'ISTP'), (11, 'ISFJ'), (12, 'ISFP'), 
        (13, 'INTJ'), (14, 'INTP'), (15, 'INFJ'), (16, 'INFP'), 
    )

    MBTI = models.CharField(max_length=50,choices=mbti_choice)