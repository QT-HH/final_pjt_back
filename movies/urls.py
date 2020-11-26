from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list_popular),
    path('recent/', views.movie_list_recent),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/comments/', views.comment_list_create, name='comment_list_create'),
    path('comments/<int:comment_pk>/', views.comment_update_delete),
    path('recommanded_1/', views.recommanded_1, name='recommanded_1'),
    path('recommanded_2/', views.recommanded_2, name='recommanded_2'),
    path('recommanded_3/', views.recommanded_3, name='recommanded_3'),
    path('recommanded_comment/', views.recommanded_comment),
]