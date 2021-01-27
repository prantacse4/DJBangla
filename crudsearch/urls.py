from django.contrib import admin
from django.urls import path
from crudsearch import views

urlpatterns = [
    path('',views.crudsearch, name="crudsearch"),
    path('student/',views.crudsearch_student, name="crudsearch_student"),
    path('detete_project/<int:id>/',views.crudsearch_delete_project, name="crudsearch_delete_project"),
    path('detete_student/<int:id>/',views.crudsearch_delete_student, name="crudsearch_delete_student"),
    path('crudsearch_remove_project/<int:id>/',views.crudsearch_remove_project, name="crudsearch_remove_project"),
    path('crudsearch_removed/',views.crudsearch_removed, name="crudsearch_removed"),
    path('crudsearch_removed_delete_project/<int:id>/',views.crudsearch_removed_delete_project, name="crudsearch_removed_delete_project"),



]
