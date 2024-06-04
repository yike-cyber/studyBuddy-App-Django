from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models.functions import MD5
from itertools import chain # for list
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



from .models import Room ,Topic,Message,User,ReplyMessage,MessageLog,RoomLog
from . forms import RoomForm,UpdateUserForm

from .common import mainView
from .online_status import update_online_status,clear_online_status

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                update_online_status(None,user,request)
                return redirect('home')
            else:
                messages.error(request, 'Incorrect password.')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
    
    context = {'page': page}
    return render(request, 'base/login_register.html', context)
    
def logoutUser(request):
    clear_online_status(None,request.user,request)
    logout(request)
    return redirect('login')

def registerPage(request):
    # form = UserRegistrationForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username').lower()
        password  = request.POST.get('password')
        password2 = request.POST.get('password2')
    
        if User.objects.filter(username =username):
            messages.error(request,'user name already exist!')
            return redirect('register')
        
        elif User.objects.filter(email =email):
            messages.error(request,'email already exist!')
            return redirect('register')
        
        elif password != password2:
            messages.error(request,'password mismatch!')
            return redirect('register')
        
        else:
           user = User.objects.create(username = username,password = password,email= email)
           user.save()
           login(request,user)
           return redirect('login')
        
    return render(request,'base/login_register.html')

@login_required(login_url='login')
def home(request):
    q = request.GET.get('q')
    context = mainView(request,q)
  
    return render(request,'base/home.html',context)

@login_required(login_url='login')
def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.filter(is_deleted = False).order_by('-created')
     
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
            
        )
        room.participants.add(request.user)
        return redirect('room',pk = room.id)
    
    replies = []
    for message in room_messages:
        reply = ReplyMessage.objects.filter(message=message)
        replies.append(reply)
    
    replies =  list(chain(*replies))
    print(replies)
    context = {'room':room,
               'current_user': request.user,
               'room_messages':room_messages,
                'visible_words':100,
               'participants':participants,
               'replies':replies
               }
             
    return render(request,'base/room.html',context )

@login_required(login_url='login')
def getTopics(request):
    topics = Topic.objects.all()
    context  = {
        'topics':topics,
    }
    
    return render(request,'base/show_topics.html',context)

@login_required(login_url='login')
def getActivities(request):
    user = User.objects.get(username = request.user.username)
    room_messages = user.message_set.all().order_by('-created')
    context  = {
        'room_messages':room_messages,
        'visible_words':5
    }
    
    return render(request,'base/show_recent.html',context)


@login_required(login_url='login')
def userProfile(request,pk):
    user = User.objects.get(id = pk)
    rooms = user.room_set.all()
    
    topics = Topic.objects.all()
    room_messages = user.message_set.filter(is_deleted = False)
    
    context = {'user':user,
               'rooms':rooms,
               'room_messages':room_messages,
               'topics':topics,
               'visible_words':5,
               }
    return render(request,'base/profile.html',context)

@login_required(login_url='login')
def editProfile(request,pk):
    user = User.objects.get(id = pk)
    rooms = user.room_set.all()
    
    topics = Topic.objects.all()
    room_messages = user.message_set.all()
    if request.method =='POST':
       
        user = User.objects.get(id=pk)
        
        if User.objects.filter(username =request.POST.get('username')).exclude(username = user.username).count() !=0:
            messages.error(request,'user name exist change other')
            return redirect('edit-profile',pk)
        
        elif User.objects.filter(email =request.POST.get('email')).exclude(email = user.email).count()!=0:
            messages.error(request,'email already exist change other')
            return redirect('edit-profile',pk)
        else: 
             user.email = request.POST.get('email')
             user.username = request.POST.get('username')
             user.bio = request.POST.get('bio')
             user.name = request.POST.get('name')
             print(request.FILES.get('profileImage'))
            #  if request.POST.get('password') != None:
            #     user.password  = MD5(request.POST.get('password'))
             if request.FILES.get('profileImage') == None:
                print(user.avatar)
                user.avatar = user.avatar
             else:
                user.avatar = request.FILES.get('profileImage')
             user.save()
             print(user.avatar)
             return redirect('home')
        
    context = {'user':user,
               'rooms':rooms,
               'room_messages':room_messages,
               'topics':topics,
               'visible_words':5,
               }
    return render(request,'base/edit_profile.html',context)

@login_required(login_url='login')
def createRoom(request):
    topics = Topic.objects.all
     
    if request.method =='POST':
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
       
        room =  Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')           
            
        ) 
        room.save()
        if 'roomImage' in request.FILES:
            room.roomImage = request.FILES['roomImage']
            room.save()
            
        return redirect('create-room')
        
    context = {
               'topics':topics}
    return render(request,'base/room_form.html',context) 

@login_required(login_url='login')
def updateRoom(request,pk):
    room  = Room.objects.get(id = pk)
    form  = RoomForm(instance = room)
    topics = Topic.objects.all

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!.')
    
    if request.method =='POST':
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')
    
    context = {'room':room,
               'type':'update',
               'topics':topics
               }
    
    return render(request,'base/room_form.html',context )

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id =pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!.')
    
    if request.method == "POST":
         room_log = RoomLog.objects.create(room = room)
         room_log.save()
         room.is_deleted = True
         room.save()
         return redirect('home')
    context = {'room':room}
    return render(request,'base/delete.html',context)
    
    
@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Message.objects.get(id =pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here!!.')
    
    if request.method == "POST":
         message_log = MessageLog.objects.create(message = message)
         message_log.save()
         print(message_log.message.body[:5])
         message.is_deleted = True
         message.save()
         print(message_log.message.body[:5])

         return redirect('home')
    
    context = {'message':message}
    return render(request,'base/delete.html',context)
    
def editMessage(request,pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here!!.')
    
    if request.method == "POST":
         message.body = request.POST.get('body')
         message.save()
         return redirect('home')
    
    q = request.GET.get('q')
    message = {'message':message}
    main_view = mainView(request,q)
    main_view.update(message)
    print(message)
    return render(request,'base/edit_message.html',main_view)



def replyMessage(request):
    if request.method == 'POST':
        print('GET method is done',)
        replier = User.objects.get(email = request.POST.get('replier'))
        message = Message.objects.get(id =request.POST.get('messageId'))
        room_id  = message.room.id
        replied_text = request.POST.get('body')
        replied_message = ReplyMessage(replier=replier,message = message,replied_text = replied_text)
        replied_message.save()
        message.num_of_replies+=1
        message.save()
        room_id = str(room_id)   
        context = {
            'data':'sucesfull'
        }     
        return JsonResponse(context)
    else:
        return redirect('home')

def editReply(request,pk):
    print(pk)
    message_replied = ReplyMessage.objects.get(id = pk)
    print(message_replied)
    if request.user != message_replied.replier:
        return HttpResponse('You are not allowed here!!.')
    
    if request.method == "POST":
         message_replied.replied_text = request.POST.get('body')
         message_replied.save()
         return redirect('home')
    
    q = request.GET.get('q')
    message_replied = {'message':message_replied}
    main_view = mainView(request,q)
    main_view.update(message_replied)
    return render(request,'base/edit_reply.html',main_view)
 
def deleteReply(request,pk):
    replied_message = ReplyMessage.objects.get(id =pk)
    roomId = replied_message.message.room.id
    if request.user != replied_message.replier:
        return HttpResponse('You are not allowed here!!.')
    
    if request.method == "POST":
        message = replied_message.message
        message.num_of_replies-=1
        message.save()
        replied_message.delete()
        return redirect('room',pk=roomId)
    
    context = {'message':replied_message}
    return render(request,'base/delete.html',context)
        
           
def likeMessage(request, pk, userId):
    user = User.objects.get(id=userId)
    message = Message.objects.get(id=pk)
    
    if user in message.liker.all():
        message.liker.remove(user)
        message.num_of_likes -= 1
    else:
        message.liker.add(user)
        message.num_of_likes += 1
        
    message.save()
    roomId = message.room.id
    return redirect('room', pk=roomId)

         
    