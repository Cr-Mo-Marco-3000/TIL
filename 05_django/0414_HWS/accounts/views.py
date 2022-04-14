from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm


@require_http_methods(['POST', 'GET'])
def login(request):
    if request.user.is_authenticated:
        redirect('todos:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'todos:index')
    else:
        form = AuthenticationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/login.html', context)



@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.user.is_authenticated:
        redirect('todos:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
    