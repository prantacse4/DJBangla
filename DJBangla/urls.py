from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from basics import views
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatternsForApps = [
    path('', include('basics.urls')),
    path('crudsearch/', include('crudsearch.urls')),
    path('imagecrud/', include('imagecrud.urls')),
    path('multiauth/', include('multiauth.urls')),
]
urlpatterns += urlpatternsForApps

wrongurls = [
    # re_path('home/.*/', views.starter, name='starter'),
    re_path('.*/', views.wrongurl, name='wrongurl'),
]
urlpatterns += wrongurls
