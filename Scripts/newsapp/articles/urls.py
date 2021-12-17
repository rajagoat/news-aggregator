from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('note_create/', views.note_create, name='note_create'), # TEST
    path('<slug:slug>/', views.article_details, name='details'),
]
