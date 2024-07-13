from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "quotes"


urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('author_page/<int:author_id>', views.author_page, name='author_page'),
    path('tag_page/<str:tag>', views.tag_page, name='tag_page'),
    path('users/', include('users.urls')),
    path('nauthor', views.nauthor, name="nauthor"),
    path('nquote', views.nquote, name="nquote"),
]
