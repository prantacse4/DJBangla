from django.contrib import admin
from django.urls import path
from multiauth import views

urlpatterns = [
    path('',views.multiauth, name="multiauth"),


]