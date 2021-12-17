from django.urls import path
from articles.api import views

app_name = 'articles'

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    path('topics/', views.topics, name='topics'), 
    path('newssource/', views.newssource, name='newssource'),
]
