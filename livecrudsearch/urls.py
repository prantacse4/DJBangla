from django.contrib import admin
from django.urls import path
from livecrudsearch import views

urlpatterns = [
    path('',views.livecrudsearch, name="livecrudsearch"),
]
