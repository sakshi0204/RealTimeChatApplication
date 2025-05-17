from django.urls import path
from .views import HomeView, RoomView,sign_up
urlpatterns=[
    path("login/",HomeView, name="login"),
    path('',sign_up, name='signup'),

    path("<str:RoomName>/<str:UserName>/", RoomView,name="room")
]   

