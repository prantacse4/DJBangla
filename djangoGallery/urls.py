from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery, name="gallery"),
    path('albums/<int:id>/',views.albums, name="albums"),
    path('addPhoto/',views.add_photo, name="add_photo"),
    path('addPhoto/album/<int:id>',views.add_photo_from_album, name="add_photo_from_album"),
    path('delete/album/<int:id>',views.delete_album, name="delete_album"),
    path('delete/photos/<int:id>',views.delete_photos, name="delete_photos"),
    path('album/delete/photos/<int:id>',views.delete_photos_from_album, name="delete_photos_from_album"),

]