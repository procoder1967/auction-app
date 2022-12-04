from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import User, Profile
from .forms import Login, SignupForm

# Create your views here.
def base_index(request):
    return HttpResponse("Hello, world. You're at the base index.")

# def sign_up(request):

#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         username = form.cleaned_data['username']
#         email = form.cleaned_data['email']
#         password = form.cleaned_data['password']
#         newUser = User.objects.create(email = email)
#         newUser.set_password(password)
#         newUser.save()

#         user =auth.authenticate(email=email, password =password)

#         if user is not None:
#             auth.login(request,user)
#             return redirect('') #FILL IN
    
#     return render(request, 'auctionapp/auth/signup.html', {'form': SignupForm})

def login_view(request):
    form = Login()
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user =auth.authenticate(email=email, password =password)
            if user is not None:
                auth.login(request,user)
                return redirect('') #FILL IN
            
            return render(request, 'error.html', {
                'error': 'User not registered. Sign up first.'
            })

        # invalid form
        return render(request, 'auctionapp/auth/login.html', {
            'form': form
        })

    return render(request, 'auctionapp/auth/login.html', {'form': form})


@login_required
def GET_Items(request):
    #mounted
    return

@login_required
def Add_Items(request):
    return

def GET_Search(request):
    return

    
def update_profile(request):
    return

@login_required
def message(request):
    return

def message_winner(request):
    #cron job
    return