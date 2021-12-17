from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('note_create/', views.note_create, name='note_create'), # TEST
    path('note_delete/', views.note_create, name='note_delete'), # TEST
    path('comment_create/', views.comment_create, name='comment_create'), # TEST
    path('rating_create/', views.rating_create, name='rating_create'), # TEST
    path('<slug:slug>/', views.article_details, name='details'),
]
