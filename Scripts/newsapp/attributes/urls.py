from django.urls import path
from . import views

urlpatterns = [
    path('authNotes', views.authNotes, name='authNotes'),
    path('notes', views.notes, name='notes'),
    path('comments', views.comments, name='comments'),
    path('ratings', views.ratings, name='ratings'),
]
