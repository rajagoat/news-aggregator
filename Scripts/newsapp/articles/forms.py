from django import forms
from django.db.models import fields
from attributes import models

class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['about']

class CreateAuthNote(forms.ModelForm):
    class Meta:
        model = models.AuthNote
        fields = ['article_id','title','body']

class CreateRating(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = ['article_id','refer_to_friend', 'rating']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['article_id', 'comment']