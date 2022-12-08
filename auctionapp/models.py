from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    city = models.CharField(max_length=50)
    date_of_birth = models.DateField(default='1970/01/01')
    messages = models.ManyToManyField(to='self',symmetrical=False,blank=True)
    Profile  = models.OneToOneField(to='Profile',null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    
    def to_dict(self):
        return{
            'id':self.id,
            'username':self.username,
            'email':self.email,
            'date_of_birth':self.date_of_birth,
            'messages':self.messages,
            'Profile':self.Profile,
        }
    
    def messages_senrec(self,other):
        #someone sends you a message
        m1 = Messages.objects.filter(sender = other, receiver = self)

        #you send a message to someone
        m2 = Messages.objects.filter(sender = self, sender = other)

        return m1.union(m2).order_by('-time_sent')

class Profile(models.Model):
    username = models.ForeignKey(max_length=50,to='User',related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics',blank=True)
    bio = models.TextField(max_length=500,blank=True)
    
    def __str__(self):
        return f"{self.bio}"

    def to_dict(self):
        return {
            'username': self.username,
            'bio': self.text,
            'image': self.image.url if self.image else None,
        }

class Item(models.Model):
    start_bid = models.DecimalField(max_digits=6,decimal_places=2)
    bid = models.DecimalField(max_digits=6,decimal_places=2)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='item_pics',blank=True)
    bid_time_finish = models.DateTimeField(default=timezone.now)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}" f"{self.description}"
    
    def to_dict(self):
        return{
            'id':self.id,
            'start-bid':self.start_bid,
            'bid':self.bid,
            'title':self.title,
            'description':self.description,
            'image':self.image,
            'bid_time_finish':self.bid_time_finish,
            'bought':self.bought,
        }

class Messages(models.Model):
    question_message = models.CharField(max_length=500)
    time_sent = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(to=User,related_name='sent_messages',on_delete=models.CASCADE)
    receiver = models.ForeignKey(to=User,related_name='received_messages',on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.sender} to f{self.receiver})"
    
    def to_dict(self):
        return{
            'id':self.id,
            'question_message':self.question_message,
            'time_sent':self.time_sent.strftime("%Y-%d-%mT%H:%M"),
            'sender':self.sender.username,
            'receiver':self.receiver.username,
        }


