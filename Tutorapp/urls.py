from django.contrib import admin
from django.urls import path, include
from .views import BlogDetailView, BlogListView, TimeCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("session/new/", TimeCreateView.as_view(), name="time_add"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("", BlogListView.as_view(), name="home")
]