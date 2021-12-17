from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<slug:slug>/', views.article_details, name='details'),
    path('search_results', views.search_results, name='search_results'),
    path('filter_results/<slug:slug>/', views.filter_results, name='filter_results')
]
