from django.conf.urls import  url,include
from django.contrib.auth import  views as auth_views
from . import views

app_name = 'user_interface'

urlpatterns = [
        url(r'^user_interface', views.getUser_input.as_view(),name='getUser_input'),
]
