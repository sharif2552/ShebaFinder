from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/services/', include('services.urls')),
    path('api/search/', include('search.urls')),
    path('api/reviews/', include('reviews.urls')),
]
