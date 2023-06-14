from django.urls import reverse

from django.contrib import messages

from users.forms import user_creation_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponseRedirect

def register_view(request):
    if not request.user.is_authenticated:
        form = user_creation_form()
        if request.method == 'POST':
            form = user_creation_form(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('users:login'))
        context = {'form': form}
        return render(request, 'register/register.html', context)
    else:
        return redirect('/')    
    

def login_view(request):                                              
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            email = User.objects.get(email=email)
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, 'Incorrect username or password')
    return render(request, 'login/login.html')

@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')