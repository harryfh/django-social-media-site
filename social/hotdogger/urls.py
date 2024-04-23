from django.urls import path
from .views import dashboard, profile_list, profile, blog_post

app_name = "hotdogger"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path('blog/<int:pk>/', blog_post, name='blog_post'),
]