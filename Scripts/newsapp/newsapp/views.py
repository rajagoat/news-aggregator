from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Test')

def user(request):
    return render(request, 'user.html')

def author(request):
    return render(request, 'author.html')