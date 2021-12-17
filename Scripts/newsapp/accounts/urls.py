from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('signup-reader', views.signup_reader_view, name='signup-reader'),
    path('signup-author', views.signup_author_view, name='signup-author'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]

