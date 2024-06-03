from django.contrib.auth.models import User
from django.db.models import Q

from .models import Room,Topic,Message

def mainView(request,q):
        q = q if q != None else ''
        print(q)

        rooms = Room.objects.filter(Q(
                Q(topic__name__icontains = q)|
                Q(description__icontains = q)|
                Q(name__icontains = q)
                  )&Q(is_deleted = False)
                
                ) 
        topic = Topic.objects.all()
        room_count = rooms.count()
        room_messages = Message.objects.filter(Q(room__topic__name__icontains=q)&
                                               Q(is_deleted = False)&
                                               Q(room__is_deleted = False)
                                               
                                               )
        
        
        context ={'rooms':rooms,
                'room_count':room_count,
                'topics':topic,
                'room_messages':room_messages,
                'visible_words':5,
                    
                }
        return context