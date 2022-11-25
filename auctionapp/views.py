from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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