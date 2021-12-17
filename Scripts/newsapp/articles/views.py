from django.shortcuts import render
from .models import Article
from attributes.models import Note
from django.http import HttpResponse

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    notes = Note.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles, 'notes':notes})

def article_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    return render(request, 'articles/article_details.html', {'article': article})