from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basics.urls')),
    path('crudsearch/', include('crudsearch.urls')),
    path('livecrudsearch/', include('livecrudsearch.urls')),
]
