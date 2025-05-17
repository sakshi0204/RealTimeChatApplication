from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from .models import Room, Message
from .forms import SignUpForm
from django.core.files.storage import FileSystemStorage

# Home page for login
def HomeView(request):
    if request.method == "POST":
        username = request.POST["username"]
        room_name = request.POST["room"]

        # Check if the room exists
        try:
            existing_room = Room.objects.get(room_name=room_name)
        except Room.DoesNotExist:
            messages.error(request, "Room does not exist. Please enter a valid room name.")
            return render(request, "login.html")

        # Validate if the username exists using the custom user model
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Incorrect Username. Please enter a valid username.")
            return render(request, "login.html")

        # Redirect to the room if validation is successful and give url as we mentioned in url.py file
        return redirect("room", RoomName=room_name, UserName=username)
    
    return render(request, "login.html")

# Room page for messaging
def RoomView(request, RoomName, UserName):
    try:
        existing_room = Room.objects.get(room_name=RoomName)
    except Room.DoesNotExist:
        messages.error(request, "The room you're trying to access does not exist.")
        return redirect('login')

    if request.method == 'POST':
        message_text = request.POST.get('message')
        uploaded_file = request.FILES.get('file')

        if message_text or uploaded_file:
            # In this message object is created in the memory but its not save in db
            message = Message(room=existing_room, sender=UserName, message=message_text)
            
            if uploaded_file:
                fs = FileSystemStorage()
                filename = fs.save(uploaded_file.name, uploaded_file)
                file_url = fs.url(filename)
                message.file = file_url

            message.save()
            return redirect('room', RoomName=RoomName, UserName=UserName)

    get_messages = Message.objects.filter(room=existing_room)
    context = {
        "messages": get_messages,
        "user": UserName,
        "room_name": existing_room.room_name
    }
    return render(request, "room.html", context)

# Signup page
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log in the user after signup
            return redirect('login')  # Redirect to login page after signup
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
