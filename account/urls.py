from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="account/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("register/", views.SignUp, name="signup"),
    path("", views.home, name="home"),
    path("aboutus/", views.aboutus, name="about-us"),
    path("contact/", views.contact, name="contact"),
]
