from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('user-profile/<str:pk>/',views.userProfile,name='user-profile'),
    path('edit-profile/<str:pk>/',views.editProfile,name='edit-profile'),
    
    
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    path('edit-message/<str:pk>/',views.editMessage,name='edit-message'),
]
