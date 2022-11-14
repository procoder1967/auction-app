from django.urls import path
from . import views

urlpatterns = [
    path('',views.base_index,name='base_index'),
]
