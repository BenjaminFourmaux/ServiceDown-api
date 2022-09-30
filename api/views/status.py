from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import CurrentStatus, Status
from api.serializers import CurrentStatusSerializer, CurrentStatusWithStatsSerializer
from api.serializers.status import StatusSerializer
from api.utils import MethodNotAllowed
from django.db.models import Q

from api.utils.check_controls import CheckControlsUtils


class StatusViewSet(viewsets.ModelViewSet):
    queryset = CurrentStatus.objects
    serializer_class = CurrentStatusSerializer

    # <editor-fold desc="Endpoints Disabled">
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed

    def update(self, request, *args, **kwargs):
        # Partner programs
        raise MethodNotAllowed

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed

    # </editor-fold>

    @action(methods=['GET'], detail=False, url_path='types', url_name='types status')
    def types(self, request, *args, **kwargs):
        status_type = Status.objects.all()
        serializer = StatusSerializer(status_type, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='service/(?P<service_id>\w+)/country/(?P<country_id>\w+)',
            url_name='service status')
    def service_status_by_country(self, request, service_id, country_id, *args, **kwargs):
        # TODO:  make it with 'fields' url param
        # Check
        CheckControlsUtils.check_service_country(service_id, country_id)

        current_status = self.queryset.filter(Q(service=service_id) & Q(country=country_id)).first()

        serializer = CurrentStatusWithStatsSerializer(current_status, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='current_outage', url_name='get services current outage')
    def services_current_outage(self, request, *args, **kwargs):
        outage_status_q = Q(status__id=3) | Q(status__id=2)

        if 'country' in request.GET and 'count' in request.GET:
            CheckControlsUtils.check_country(request.GET['country'])

            services_outage = self.queryset.filter(
                outage_status_q
                &
                Q(country__id=request.GET['country'])
            ).order_by('-status')[:int(request.GET['count'])]

        elif 'country' in request.GET:
            CheckControlsUtils.check_country(request.GET['country'])

            services_outage = self.queryset.filter(
                outage_status_q
                &
                Q(country__id=request.GET['country'])
            ).order_by('-status')
        elif 'count' in request.GET:
            services_outage = self.queryset.filter(outage_status_q).order_by('-status')[:int(request.GET['count'])]
        else:
            services_outage = self.queryset.filter(outage_status_q).order_by('-status')

        serializer = self.serializer_class(services_outage, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
