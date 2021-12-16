from django.db import models
from django.db.models.fields import PositiveIntegerField

# Create your models here.
class AuthNote(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    auth_note_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)

class Note(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    note_id = models.BigAutoField(primary_key=True)
    about = models.CharField(max_length=1000)

class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    comment_date = models.DateTimeField()
    article_id = models.BigAutoField(primary_key=True)

class Rating(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    rating_id = models.BigAutoField(primary_key=True)
    refer_to_friend = models,PositiveIntegerField()
