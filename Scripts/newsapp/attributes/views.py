from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def authNotes(request):
    return HttpResponse('authNotes')

def notes(request):
    return HttpResponse('notes')

def comments(request):
    return HttpResponse('comments')

def ratings(request):
    return HttpResponse('ratings')