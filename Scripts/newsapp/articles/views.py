from django.shortcuts import redirect, render
from attributes.models import Note, Rating, Comment
from .models import Article, Topic
from . import forms

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    notes = Note.objects.all()
    topics = Topic.objects.all()
    context = {'articles': articles, 'topics': topics, 'notes': notes}
    return render(request, 'articles/article_list.html', context)

def article_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    comments = Comment.objects.all()
    ratings = Rating.objects.all()
    return render(request, 'articles/article_details.html', {'article': article, 'comments': comments, 'ratings': ratings})

# @login_required(login_url="/accounts/login/")
def note_create(request):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            return redirect('/articles/')
        
    else:
        form = forms.CreateNote()
    
    return render(request, 'articles/note_create.html', { 'form':form })

# @login_required(login_url="/accounts/login/")
def auth_note_create(request):
    if request.method == 'POST':
        form = forms.CreateAuthNote(request.POST)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            return redirect('/articles/')
        
    else:
        form = forms.CreateAuthNote()
    
    return render(request, 'articles/auth_note_create.html', { 'form':form })

# @login_required(login_url="/accounts/login/")
def comment_create(request):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            return redirect('/articles/')
        
    else:
        form = forms.CreateComment()
    
    return render(request, 'articles/comment_create.html', { 'form':form })

# @login_required(login_url="/accounts/login/")
def rating_create(request):
    if request.method == 'POST':
        form = forms.CreateRating(request.POST)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            return redirect('/articles/')
        
    else:
        form = forms.CreateRating()
    
    return render(request, 'articles/rating_create.html', { 'form':form })

def search_results(request):
    if request.method == "POST":
        searched = request.POST['search']
        results = Article.objects.filter(name__icontains=searched)
        articles = Article.objects.all()
        context = {'articles': articles, 'searched': searched, 'results': results}
        return render(request, 'articles/search_results.html', context)
    else:
        return render(request, 'articles/search_results.html', {})

def filter_results(request, slug):
    filteredArticles = Article.objects.filter(topic = slug)
    context = {'slug': slug, 'filteredArticles': filteredArticles}
    return render(request, 'articles/filter_results.html', context)
