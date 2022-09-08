from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Service, StatsReport1H, StatsReport24H
from api.serializers import ServiceSerializer, ServiceSerializerFields, StatsReport1HSerializer, \
    StatsReport24HSerializer
from api.utils import MethodNotAllowed
from api.utils.view import ViewUtils


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects
    serializer_class = ServiceSerializer
    serializer_fields_class = ServiceSerializerFields

    # <editor-fold desc="Endpoints Disabled">
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed
    # </editor-fold>

    def retrieve(self, request, *args, **kwargs):
        # Checkout
        service = ViewUtils.check_service(self.get_object().id)

        if 'fields' in request.GET:
            fields = request.GET.get('fields').split(',')

            output = self.serializer_fields_class(service, many=False, fields=tuple(fields))
        else:
            output = self.get_serializer(service, many=False)

        return Response(output.data, status=status.HTTP_200_OK)

    # <editor-fold desc="Stats Report">
    @action(methods=['GET'], detail=True, url_path='country/(?P<country_id>\w+)/stats_1h', url_name='stats report 1h')
    def stats_report_1h_with_country(self, request, pk, country_id):
        # Checkout
        ViewUtils.check_service_country(self.get_object().id, country_id)

        stats_report = StatsReport1H.objects.filter(Q(country__id=country_id) & Q(service=self.get_object())).first()
        serializer = StatsReport1HSerializer(stats_report, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=['GET'], detail=True, url_path='country/(?P<country_id>\w+)/stats_24h', url_name='stats report 24h')
    def stats_report_24h_with_country(self, request, pk, country_id):
        # Checkout
        ViewUtils.check_service_country(self.get_object().id, country_id)

        stats_report = StatsReport24H.objects.filter(Q(country__id=country_id) & Q(service=self.get_object())).first()
        serializer = StatsReport24HSerializer(stats_report, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # </editor-fold>
