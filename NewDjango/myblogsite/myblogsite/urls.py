from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Only here
    path('', include('blog.urls')),  # Include blog URLs
]
