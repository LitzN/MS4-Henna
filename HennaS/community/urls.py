from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_posts, name="view_posts"),
    path('add_post/', views.add_post, name="add_post"),
]
