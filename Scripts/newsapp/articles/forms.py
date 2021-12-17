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
        fields = ['title','body','article_id']

class CreateRating(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = ['refer_to_friend', 'rating', 'article_id']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['article_id', 'comment']