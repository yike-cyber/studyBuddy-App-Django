from django.contrib.auth.models import User
from django.db.models import Q

from .models import Room,Topic,Message

def mainView(request,q):
        
        q = request.GET.get(q) if request.GET.get(q) != None else ''
        rooms = Room.objects.filter(
                Q(topic__name__icontains = q)|
                Q(description__icontains = q)|
                Q(name__icontains = q)
                
                ) 
        topic = Topic.objects.all()
        room_count = rooms.count()
        room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
        
        
        context ={'rooms':rooms,
                'room_count':room_count,
                'topics':topic,
                'room_messages':room_messages,
                'visible_words':5,
                    
                }
        return context