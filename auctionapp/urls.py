from django.urls import path
from . import views
from auctionapp.views import login_view, base_index

urlpatterns = [
    path('',views.login_view,name='check'),
    # path('signup', views.sign_up, name= 'sign_up'),
]
