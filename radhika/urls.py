"""radhika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Home.views import home, index
from aboutus.views import aboutus
from booking.views import booking_done, booking, new_appointment
from contactus.views import contact
from register.views import register, reg_page
from services.views import service
from sign.views import signup_login, signup, signin
from update_cancle.views import update_cancle, update, cancle

urlpatterns = {
    path('home/', home),
    path('index/', index),
    path('signup_login/', signup_login),
    path('signup/', signup),
    path('signin/', signin),
    path('register/', register),
    path('reg_page/', reg_page),
    path('aboutus/', aboutus),
    path('contact/', contact),
    path('service/', service),
    path('booking/', booking),
    path('booking_done/', booking_done),
    path('index/', index),
    path('update_cancle/', update_cancle),
    path('update/', update),
    path('cancle/', cancle),
    path('new_appointment/', new_appointment),

}

