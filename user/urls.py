from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("login/", views.userLogin, name="login"),
    path("logout/", views.userLogout, name="logout"),
    path("register/", views.userRegister, name="register"),
    path("userDashboard/", views.userDashboard, name="userDashboard"),
]
