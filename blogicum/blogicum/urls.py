from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include blog URLs
    path('pages/', include('pages.urls')),  # Include pages URLs
]
