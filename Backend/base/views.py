from django.shortcuts import render


rooms = [
    {'id':1,'name':'lets learn pytho.'},
    {'id':2,'name':'Design with me.'},
    {'id':3,'name':'Frontend developers.'}
]

def home(request):
    context = {'rooms':rooms,}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = None
    for room in rooms:
         if room['id'] == int(pk):
             room = room
    context = {'room':room,}
             
    return render(request,'base/room.html',context )