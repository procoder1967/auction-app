#messages, upload, 

from django.http.response import HttpResponseBadRequest, JsonResponse, HttpResponse, Http404
from django.shortcuts import get_object_or_404
from .models import User, Profile, Item
from django.contrib.auth.decorators import login_required

@login_required
def change_image(request):
    user = request.user

    if 'image' in request.FILES:
        image = request.FILES['image']
        '''if not user.profile:
            # if user doesn't have a profile yet
            # need to create a profile first
            profile = Profile(text='')
            profile.save()
            user.profile = profile
            user.save()'''
        #assumes profile has already been created before user can run this
        user.profile.image  = image
        user.profile.save()
        return HttpResponse(user.profile.image.url)
    else:
        raise Http404('No image received')


@login_required
def addItemImage(request):
    user = request.user

    if 'image' in request.FILES:
        image = request.FILES['image']
        if not user.item:
            item = Item()
            item.save()
            user.item = item
            user.save()
        user.item.image  = image
        user.item.save()
        return HttpResponse(user.item.image.url)
    else:
        raise Http404('No image received')
