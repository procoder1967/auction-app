from django.http import HttpResponse,HttpRequest,Http404,JsonResponse
import json
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import User, Profile,Item
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
def GET_Items(request: HttpRequest)->HttpResponse:
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })

@login_required
def Add_Items(request):
    return

def GET_Search(request):
    return

    
def profile(request):
    user = request.user

    if 'bio' in request.POST and request.POST['bio']:
        bio = request.POST['bio']
        if user.profile:
            user.profile.bio = bio
            user.profile.save()
        else:
            profile = Profile(bio=bio, username = 'Anon')
            profile.save()
            user.profile = profile
        user.save()
    
    info = {
        'user':user,
        'page': user.profile,
        'session_key': request.session.session_key,
        'meta': request.META,
        
        }
    #not sure about this tbh
    return render(request, 'auctionapp/frontend/src/Home.vue', info)
    





@login_required
def message(request):
    return

def message_winner(request):
    #cron job
    return