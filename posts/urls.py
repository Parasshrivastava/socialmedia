# from django.contrib import admin
from django.urls import path
from .import views
# from django.contrib.auth import views as auth_view

urlpatterns = [
    path('create/',views.post_create,name='index'),
    path('feed',views.feed,name='feed'),
    path('like',views.like_post,name='like')
    

]