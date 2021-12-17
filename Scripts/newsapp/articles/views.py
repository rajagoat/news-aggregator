from django.shortcuts import render
from .models import Article, Topic, NewsSource
from django.http import HttpResponse

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    topics = Topic.objects.all()
    context = {'articles': articles, 'topics': topics}
    return render(request, 'articles/article_list.html', context)

def article_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    return render(request, 'articles/article_details.html', {'article': article})