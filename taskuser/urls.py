# from django.conf.urls import  , include
from django.urls import path, include

from . import views as core_views



urlpatterns = [
    path('',core_views.home, name='home'),
    path('login/', core_views.login, name="login"),
    path('signup/', core_views.signup, name='signup'),
]