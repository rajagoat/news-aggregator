from django.shortcuts import redirect, render
from .models import Article
from attributes.models import Note
from django.http import HttpResponse
from . import forms

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    notes = Note.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles, 'notes':notes})

def article_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    return render(request, 'articles/article_details.html', {'article': article})

# @login_required(login_url="/accounts/login/")
def note_create(request):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST)
        if form.is_valid:
            # save article to db
            return redirect('articles/article_list.html')
        
    else:
        form = forms.CreateNote()
    
    return render(request, 'articles/note_create.html', { 'form':form })