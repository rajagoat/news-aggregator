from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login')
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

@login_required(login_url='/accounts/login')
def article_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    return render(request, 'articles/article_details.html', {'article': article})