from django.core.paginator import Paginator
from django.db.models import Q
from django.db import models
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Service, StatsReport1H, StatsReport24H, CurrentStatus, Country
from api.serializers import ServiceSerializer, ServiceSerializerFields, StatsReport1HSerializer, \
    StatsReport24HSerializer, PagingSerializer, CurrentStatusSerializer, ServiceWithStatusSerializer
from api.utils import MethodNotAllowed, UrlParameterMissing, ServiceNotFound, SerializerUtils
from api.utils.check_controls import CheckControlsUtils


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
        service = CheckControlsUtils.check_service(self.get_object().id)

        if 'fields' in request.GET:
            fields = request.GET.get('fields').split(',')

            output = self.serializer_fields_class(service, many=False, fields=tuple(fields))
        else:
            output = self.get_serializer(service, many=False)

        return Response(output.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='by_path', url_name='get country by path')
    def retrieve_by_path(self, request, *args, **kwargs):
        if 'country' in request.GET and 'path' in request.GET:
            # Get Service by country and path
            CheckControlsUtils.check_country(request.GET.get('country'))

            service = self.queryset.filter(Q(countries__in=[request.GET.get('country')]) & Q(path__exact=request.GET.get('path'))).first()
            if not service:
                raise ServiceNotFound
            serializer = self.serializer_class(service, many=False)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise UrlParameterMissing

    @action(methods=['GET'], detail=False, url_path='country/(?P<country_id>\w+)/with_status',
            url_name='services by country with status')
    def list_with_status(self, request, country_id):
        # Check
        CheckControlsUtils.check_country(country_id)

        services_by_country_with_status = CurrentStatus.objects.filter(country=country_id).order_by('service__name')

        # Pagination
        pagination = Paginator(services_by_country_with_status, 20)
        serializer = PagingSerializer(pagination, CurrentStatusSerializer)

        # Check paging index
        if 'page' in request.GET:
            paging_index = int(request.GET.get('page'))
            CheckControlsUtils.check_pagination_page_num(pagination, paging_index)
        else:
            paging_index = 1

        return Response(serializer.data(paging_index), status=status.HTTP_200_OK)

    # <editor-fold desc="Stats Report">
    @action(methods=['GET'], detail=True, url_path='country/(?P<country_id>\w+)/stats_1h', url_name='stats report 1h')
    def stats_report_1h_with_country(self, request, pk, country_id):
        # Checkout
        CheckControlsUtils.check_service_country(self.get_object().id, country_id)

        stats_report = StatsReport1H.objects.filter(Q(country=country_id) & Q(service=self.get_object())).first()

        if not stats_report:
            stats_report = StatsReport1H()
            stats_report.id = 0
            stats_report.service = self.get_object()
            stats_report.country = Country.objects.get(pk=country_id)
            stats_report = SerializerUtils.emptyStats1H(stats_report)

        serializer = StatsReport1HSerializer(stats_report, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True, url_path='country/(?P<country_id>\w+)/stats_24h', url_name='stats report 24h')
    def stats_report_24h_with_country(self, request, pk, country_id):
        # Checkout
        CheckControlsUtils.check_service_country(self.get_object().id, country_id)

        stats_report = StatsReport24H.objects.filter(Q(country=country_id) & Q(service=self.get_object())).first()

        if not stats_report:
            stats_report = StatsReport24H()
            stats_report.id = 0
            stats_report.service = self.get_object()
            stats_report.country = Country.objects.get(pk=country_id)
            stats_report = SerializerUtils.emptyStats24H(stats_report)

        serializer = StatsReport24HSerializer(stats_report, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)
    # </editor-fold>
