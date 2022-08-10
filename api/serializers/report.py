from rest_framework import serializers
from api.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'service', 'country', 'submittedAt')
