from rest_framework import generics
from services.models import Service
from services.serializers import ServiceSerializer

class ServiceSearchView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        area = self.request.query_params.get('area')
        profession = self.request.query_params.get('profession')
        if area:
            queryset = queryset.filter(area__icontains=area)
        if profession:
            queryset = queryset.filter(profession__icontains=profession)
        return queryset
