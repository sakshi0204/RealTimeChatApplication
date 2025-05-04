from django.urls import path
from .views import HomeView, RoomView
urlpatterns=[
    path("",HomeView, name="login"),
    path("<str:RoomName>/<str:UserName>/", RoomView,name="room")
]   