from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, ProfileRegisterForm, AuthorRegisterForm
from .models import Profile, Reader, Author
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup_view(request):
    return render(request, 'accounts/signup.html')

def signup_reader_view(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST, prefix='user')
        profile_form = ProfileRegisterForm(request.POST, prefix='profile')
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            if(profile_form.is_valid()):
                user.profile = Profile()
                user.profile.user = user
                user.profile.birth_date = profile_form.cleaned_data.get('birth_date')
                user.profile.address = profile_form.cleaned_data.get('address')
                user.profile.save()
                user.reader = Reader()
                user.reader.user = user
                user.reader.save()
                user.save()
                messages.success(request, f'Account: {user.username} has been successfully created!')
                login(request, user)
                return redirect('articles:list')
    else:
        user_form = UserRegisterForm(prefix='user')
        profile_form = ProfileRegisterForm(prefix='profile')
    return render(request, 'accounts/signupReader.html', {'user_form': user_form, 'profile_form':profile_form})


def signup_author_view(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST, prefix='user')
        profile_form = ProfileRegisterForm(request.POST, prefix='profile')
        author_form - AuthorRegisterForm(request.POST, prefix='author')
        if user_form.is_valid() and profile_form.is_valid() and author_form.is_valid():
            user = user_form.save()
            if(profile_form.is_valid()):
                user.profile = Profile()
                user.profile.user = user
                user.profile.birth_date = profile_form.cleaned_data.get('birth_date')
                user.profile.address = profile_form.cleaned_data.get('address')
                user.profile.save()
                user.author = Author()
                user.author.user = user
                user.author.awards = author_form.cleaned_data.get('awards')
                user.author.preferred_genre = author_form.cleaned_data.get('preferred_genre')
                user.author.save()
                user.save()
                messages.success(request, f'Account: {user.username} has been successfully created!')
                login(request, user)
                return redirect('articles:list')
    else:
        user_form = UserRegisterForm(prefix='user')
        profile_form = ProfileRegisterForm(prefix='profile')
        author_form = AuthorRegisterForm(prefix='Author')
    return render(request, 'accounts/signupAuthor.html', {'user_form': user_form, 'profile_form':profile_form, 'author_form': author_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')

@login_required(login_url='/accounts/login')
def editProfile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileRegisterForm(request.POST, instance=profile)
        if(profile_form.is_valid()):
            profile_form.save()
        return redirect('accounts:editProfile')
    else:
        profile_form = ProfileRegisterForm(instance=profile)
        return render(request, 'accounts/editProfile.html', {"form":profile_form})