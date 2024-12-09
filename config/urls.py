from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('network.urls')),
    path('network/', include('network.urls')),
    path('', include('network.urls')),

]
