
from django.urls import path,include
from account.views import  UserProfileView, UserRegisterationView,UserLoginView
from . import views
urlpatterns = [
    path('register/',UserRegisterationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    #path('DataEntry/',LeaveView.as_view(),name='DataEntry'),
    #path('register1/',views.registration,name='register1'), 
    #path('login1/',views.login1,name='login1'),   
  
]
