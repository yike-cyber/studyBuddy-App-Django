from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here. 
class User(AbstractUser):
    name  = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=200,unique=True)
    bio = models.TextField(max_length=500,null=True,blank=True)
    avatar = models.ImageField(null=True,default='avatar.svg')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username','password']
        

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 

class Room(models.Model): 
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.name

    
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey (Room,on_delete=models.CASCADE)
    body = models.TextField()
    updated  = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    num_of_likes = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ['-updated','-created']
        
    def __str__(self):
        return self.body
    
class ReplyMessage(models.Model):
    message = models.ForeignKey(Message,on_delete=models.CASCADE)
    replier = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    replied_text = models.TextField(max_length=2000)
    num_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return(self.message.room.name+self.message.body[:20]+self.replier.username)
    
# class LikeMessage(models.Model):
#     message = models.ForeignKey(Message,on_delete=models.CASCADE)
#     liker = models.ForeignKey(User,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return(self.message,self.liker)
    
class MessageLog(models.Model):
    message = models.ForeignKey(Message,on_delete=models.CASCADE)
    deleted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message.user.username+'->'+self.message.room.name+'->'+self.message.body[:5]
    
class RoomLog(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    deleted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.room.host.username+'->'+self.room.name+'->'+self.room.topic.name

      