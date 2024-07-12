from django.urls import path
from .views import ServiceSearchView

urlpatterns = [
    path('services/', ServiceSearchView.as_view(), name='service-search'),
]
