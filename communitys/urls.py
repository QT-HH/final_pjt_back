from django.urls import path
from . import views

app_name = 'communitys'
urlpatterns = [
    path('', views.review_list_create, name= 'review_list_create'),
    path('<int:review_pk>/detail/', views.review_detail, name='review_detail'),
    path('<int:review_pk>/', views.review_update_delete, name='review_update_delete'),
    path('<int:review_pk>/comments/', views.comment_list_create, name='comment_list_create'),
    path('comments/<int:comment_pk>/', views.comment_update_delete),
]