from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Country
from api.serializers import CountrySerializer
from api.utils import CountryNotAvailable, CountryShortnameNotExist
from api.utils.check_controls import CheckControlsUtils


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Country.objects
    serializer_class = CountrySerializer
    http_method_names = ['get']

    def list(self, *args, **kwargs):
        countries = self.queryset.filter(isAvailable=1).all()

        serializer = self.serializer_class(countries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # Checkout
        country = CheckControlsUtils.check_country(self.get_object().id)

        output = self.serializer_class(country)
        return Response(output.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='shortname/(?P<shortname>\w+)', url_name='get_country_by_shortname')
    def get_by_shortname(self, request, shortname):
        country = self.queryset.filter(shortname=shortname).first()

        if not country:
            raise CountryShortnameNotExist
        else:
            if not country.isAvailable:
                raise CountryNotAvailable

        serializer = self.serializer_class(country)

        return Response(serializer.data, status=status.HTTP_200_OK)
