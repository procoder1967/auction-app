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
def Item_api(request: HttpRequest)->HttpResponse:
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })
    if  request.method == 'POST':
        body = json.loads(request.body)

        item = Item(
                    start_bid = body['start_bid'],
                    bid = body['bid'],
                    title=body['title'],
                    description = body['description'],
                    image = body['image'],
                    bid_time_finish = body['bid_time_finish'],
                    bought = body['bought'],
                )
        item.save()
        return JsonResponse({
            item.to_dict()
            for item in Item.objects.all()
        })

@login_required

def GET_ItemSearch(request: HttpRequest, profile_id: int)-> HttpResponse:
    #We might change to work serilizers
    item = get_object_or_404(Item, id=profile_id) 
    if request.method =='GET':
        return JsonResponse(item.to_dict())

def profile_GET(request: HttpRequest, profile_id: int)-> HttpResponse:
    profile = get_object_or_404(Profile, id=profile_id) 
    if request.method =='GET':
        return JsonResponse(profile.to_dict())

def profile_POST(request):
    body = json.loads(request.body)
    profile = Profile(username = body['username'],bio = body['bio'], image = staticimage)
    profile.save()
    return JsonResponse({
        'profile':[
            profile.to_dict()
            for profile in Profile.objects.all()
        ]
    })
   

@login_required
def message(request):
    

def message_winner(request):
    #cron job
    return