from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "user_profile"

urlpatterns = [
    path("profile/", views.UpdatedUserProfile, name="profile"),
    path("profile/create/", views.CreateUserProfile, name="profile-create"),
    path("profile/<int:pk>/", views.UpdatedUserProfilePk, name="profile-pk"),
    path("profile/doc/<int:pk>/", views.UpdatedDocProfilePk, name="doc-profile-pk"),
    path("profile/<int:pk>/delete/", views.DeleteUserProfilePk, name="profile-delete"),
    path("profile/doc/<int:pk>/delete/", views.DeleteDocProfilePk, name="doc-profile-delete"),
]
