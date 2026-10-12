from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helloapp.urls')),
    path('', include('authapp.urls')),
    path('students/', include('studentapp.urls')),
    path('', include('studentapp.urls')),
]