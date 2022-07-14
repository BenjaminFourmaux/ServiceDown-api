from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Service
from api.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects
    serializer_class = ServiceSerializer

    @action(methods=['GET'], detail=False, url_path='list', url_name='country list')
    def list_country(self, request, pk=None):
        countries = self.queryset.filter(isAvailable=1)

        serializer = self.serializer_class(countries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
