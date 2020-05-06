from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("user_input", views.user_input, name = "user_input"),
]
