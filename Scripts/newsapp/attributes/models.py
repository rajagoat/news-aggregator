from django.db import models
from django.db.models.fields import PositiveIntegerField

from articles.models import Article

from enum import Enum

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

class RatingChoice(Enum):
    UN = "One Star"
    DE = "Two Stars"
    TR = "Three Stars"
    CA = "Four Stars"
    CI = "Five Stars"

class Rating(models.Model):
    article_id = models.ForeignKey(Article, default=None) # Switch to foreign
    rating_id = models.BigAutoField(primary_key=True)
    refer_to_friend = models.BooleanField()
    rating = models.CharField(max_length=15, choices=[(tag, tag.value) for tag in RatingChoice])

    def __str__(self):
        return str(self.rating_id)
