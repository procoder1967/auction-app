from django.urls import path
from . import views
from auctionapp.views import sign_up

urlpatterns = [
    path('',views.base_index,name='base_index'),
    path('login', sign_up, name= sign_up)
]
