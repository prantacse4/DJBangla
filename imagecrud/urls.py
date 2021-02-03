from django.contrib import admin
from django.urls import path
from imagecrud import views

urlpatterns = [
    path('',views.imagecrud, name="imagecrud"),
    path('delete_image/<int:id>/', views.imagecrud_delete_image, name="imagecrud_delete_image"),
    path('edit_image/<int:id>/', views.imagecrud_edit, name="imagecrud_edit"),
    path('crudimage_update/<int:id>/', views.crudimage_update, name="crudimage_update"),

]