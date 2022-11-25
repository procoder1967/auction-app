from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
import json

from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import User, Profile
from .forms import LoginForm, SignupForm

# Create your views here.
def base_index(request):
    return HttpResponse("Hello, world. You're at the base index.")

def sign_up(request):
    if request.POST == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')

    else:
        form = UserCreationForm()
    context = {
        'form':form
    }

    return render(request, 'register.html', context)

