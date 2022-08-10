from django.db.models import Q
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from api.models import Report
from api.serializers.report import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects
    serializer_class = ReportSerializer

    @action(methods=['GET'], detail=False, url_path='(?P<service_id>\w+)/(?P<country_id>\w+)', url_name='get report of service-country')
    def get_all_report_from_service_country(self, request, service_id, country_id):
        reports = self.queryset.filter(Q(service__id=service_id) & Q(country__id=country_id)).all()
        serializer = self.serializer_class(reports, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
