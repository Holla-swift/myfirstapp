from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('landing/', include('core.urls')),
    path('generic/', include('core.urls')),
    path('elements/', include('core.urls'))
]
