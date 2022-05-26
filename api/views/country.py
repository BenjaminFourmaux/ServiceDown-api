from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Country
from api.serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects
    serializer_class = CountrySerializer

    @action(methods=['GET'], detail=False, url_path='list', url_name='country list')
    def list_country(self, request, pk=None):
        countries = self.queryset.filter(isAvailable=1)

        serializer = self.serializer_class(countries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance: Country = self.get_object()

        if instance and instance.isAvailable:
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
