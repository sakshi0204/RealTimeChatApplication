from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Room, Message

# Create your views here.

def HomeView(request):
    if request.method == "POST":
        username=request.POST["username"]
        room=request.POST["room"]
        try:
            existing_room=Room.objects.get(room_name=room)

        except Room.DoesNotExist: 
            #new_room=Room.objects.create(room_name=room)
            messages.error(request, "Room does not exist. Please enter a valid room name.")
            return render (request,"home.html")
        return redirect("room", RoomName=room,UserName=username)
    return render (request,"home.html")

def RoomView(request,RoomName,UserName):
            existing_room=Room.objects.get(room_name=RoomName)
            get_messages=Message.objects.filter(room=existing_room)
            context={
                  "messages":get_messages,
                  "user":UserName,
                  "room_name":existing_room.room_name
            }

            return render (request,"room.html",context)