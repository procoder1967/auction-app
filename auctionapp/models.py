from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    city = models.CharField(max_length=50)
    date_of_birth = models.DateField(default='1970/01/01')
    # items_owned = 
    messages = models.ManyToManyField(to='self',symmetrical=False,blank=True)
    Profile  = models.OneToOneField(to='Profile',null=True,on_delete=models.CASCADE)


class Profile(models.Model):
    username = models.ForeignKey(max_length=50,to='User',related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics',blank=True)
    bio = models.TextField(max_length=500,blank=True)

class Item(models.Model):
    start_bid = models.DecimalField(max_digits=6,decimal_places=2)
    bid = models.DecimalField(max_digits=6,decimal_places=2)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='item_pics',blank=True)
    bid_time_finish = models.DateTimeField(default=timezone.now)
    bought = models.BooleanField(default=False)
    bid = models.ForeignKey(to='User',related_name='items_owned',on_delete=models.CASCADE)

class Messages(models.Model):
    question_message = models.CharField(max_length=500)
    time_sent = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(to='User',related_name='sent_messages',on_delete=models.CASCADE)
    receiver = models.ForeignKey(to='User',related_name='received_messages',on_delete=models.CASCADE)



