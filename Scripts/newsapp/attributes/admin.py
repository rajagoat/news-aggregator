from django.contrib import admin
from .models import AuthNote, Note, Comment, Rating

# Register your models here.
admin.site.register(AuthNote)
admin.site.register(Note)
admin.site.register(Comment)
admin.site.register(Rating)