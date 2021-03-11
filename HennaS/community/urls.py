from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_posts, name="view_posts"),
    path('add_post/', views.add_post, name="add_post"),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),
    path('delete_post/<int:post_id>/', views.delete_post, name="delete_post"),

]
