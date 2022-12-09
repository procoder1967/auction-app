from django.urls import path
from auctionapp import views, api
from auctionapp.views import login_view, base_index

urlpatterns = [
    path('',views.login_view,name='check'),
    # path('signup', views.sign_up, name= 'sign_up'),
    #path('profile/', views.profile_view, name='profile')
    path('item/',views.Item_api, name='items'),


    #path('api/change_image/', api.change_image, name = 'uploading api')
]
