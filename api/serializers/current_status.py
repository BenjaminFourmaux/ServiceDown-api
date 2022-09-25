from rest_framework import serializers
from api.models import CurrentStatus
from api.serializers import ServiceWithStatusSerializer
from api.serializers.status import StatusSerializer


class CurrentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentStatus
        fields = ('service', 'country', 'status')

    service = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    @staticmethod
    def get_service(obj):
        return ServiceWithStatusSerializer(obj.service, many=False).data

    @staticmethod
    def get_status(obj):
        return StatusSerializer(obj.status, many=False).data
