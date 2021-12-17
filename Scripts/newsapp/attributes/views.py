from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render

from .models import Note

# Create your views here.
def authNotes(request):
    return HttpResponse('authNotes')

def notes(request):
    try:
        notes = Note.objects.all()
    except Note.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'notes.html', {'notes': notes})

def comments(request):
    return HttpResponse('comments')

def ratings(request):
    return HttpResponse('ratings')