from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Country
from api.serializers import CountrySerializer
from api.utils import CountryNotAvailable, CountryNotFound


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects
    serializer_class = CountrySerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            country = self.get_object()
        except:
            raise CountryNotFound

        if country.isAvailable:
            output = self.serializer_class(country)

            return Response(output.data, status=status.HTTP_200_OK)
        else:
            raise CountryNotAvailable

    @action(methods=['GET'], detail=False, url_path='list', url_name='country list')
    def list_country(self, request, pk=None):
        countries = self.queryset.filter(isAvailable=1)

        serializer = self.serializer_class(countries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
