from django.shortcuts import redirect, render

# Create your views here.
def article_list(request):
    return render(request, 'articles/article_list.html')