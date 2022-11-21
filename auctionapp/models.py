from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    city = models.CharField(max_length=50)
    date_of_birth = models.DateField(default='1970/01/01')
    # items_owned = 
    messages = models.ManyToManyField(to='self',symmetrical=False,blank=True,null=True,on_delete=models.CASCADE)
    profile  = models.OneToOneField(to='Profile',on_delete=models.CASCADE,related_name='user',null=True)


class Profile(models.Model):
    username = models.ForeignKey(max_length=50,to='User',on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(upload_to='profile_pics',blank=True)
    bio = models.TextField(max_length=500,blank=True)

class Item(models.Model):
    start_bid = models.DecimalField(max_digits=6,min_digits=1)
    bid = models.DecimalField(max_digits=6,min_digits=1)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='item_pics',blank=True)
    bid_time_finish = models.DateTimeField(default=timezone.now)
    bought = models.BooleanField(default=False)
    bid = models.ForeignKey(to='User',on_delete=models.CASCADE,related_name='items_owned')
_

class Messages(models.Model):
    question_message = models.CharField(max_length=500)
    time_sent = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(to='User',on_delete=models.CASCADE,related_name='sent_messages')
    receiver = models.ForeignKey(to='User',on_delete=models.CASCADE,related_name='received_messages')



