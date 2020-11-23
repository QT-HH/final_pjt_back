from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
]