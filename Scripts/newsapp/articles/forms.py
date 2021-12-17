from django import forms
from django.db.models import fields
from attributes import models

class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['note_id', 'about'] # How to pass in user_id?

class CreateReview(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = ['refer_to_friend', 'rating'] # How to pass in user_id?