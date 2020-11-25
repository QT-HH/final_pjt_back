from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/comments/', views.comment_list_create, name='comment_list_create'),
    path('comments/<int:comment_pk>/', views.comment_update_delete),
    path('recommended_1/', views.recommended_1, name='recommended_1'),
]