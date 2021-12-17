from django.db import models
from django.db.models.fields import PositiveIntegerField

# Create your models here.
class AuthNote(models.Model):
    article_id = models.PositiveSmallIntegerField() # Switch to foreign
    auth_note_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.auth_note_id)

class Note(models.Model):
    user_id = models.PositiveSmallIntegerField() # Switch to foreign
    note_id = models.BigAutoField(primary_key=True)
    about = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.note_id)

class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    article_id = models.PositiveSmallIntegerField() # Switch to foreign

    def __str__(self):
        return str(self.comment_id)

class Rating(models.Model):
    article_id = models.PositiveSmallIntegerField() # Switch to foreign
    rating_id = models.BigAutoField(primary_key=True)
    refer_to_friend = models,PositiveIntegerField()

    def __str__(self):
        return str(self.rating_id)