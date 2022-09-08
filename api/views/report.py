from django.db.models import Q
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from api.models import Report
from api.serializers.report import ReportSerializer
from api.utils import MethodNotAllowed
from api.utils.view import ViewUtils


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects
    serializer_class = ReportSerializer

    # <editor-fold desc="Endpoints Disabled">
    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed
    # </editor-fold>

    @action(methods=['GET'], detail=False, url_path='(?P<service_id>\w+)/(?P<country_id>\w+)', url_name='get report of service-country')
    def list_report_from_service_country(self, request, service_id, country_id):
        # Checkout
        ViewUtils.check_service_country(service_id, country_id)

        reports = self.queryset.filter(Q(service__id=service_id) & Q(country__id=country_id)).all()
        serializer = self.serializer_class(reports, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
