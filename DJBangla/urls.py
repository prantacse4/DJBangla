from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basics.urls')),
    path('crudsearch/', include('crudsearch.urls')),
    path('crudsearch/', include('crudsearch.urls')),
    path('imagecrud/', include('imagecrud.urls')),
    path('multiauth/', include('multiauth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)