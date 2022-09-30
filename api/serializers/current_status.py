from rest_framework import serializers
from django.db.models import Q
from api.models import CurrentStatus, StatsReport24H
from api.serializers import ServiceWithStatusSerializer, StatsReport24HSerializer
from api.serializers.status import StatusSerializer
from api.utils import SerializerUtils


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


class CurrentStatusWithStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentStatus
        fields = ('currentStatus', 'stats24h')

    currentStatus = serializers.SerializerMethodField()
    stats24h = serializers.SerializerMethodField()

    @staticmethod
    def get_currentStatus(obj):
        return StatusSerializer(obj.status, many=False).data

    @staticmethod
    def get_stats24h(obj):
        stats24h = StatsReport24H.objects.filter(Q(country=obj.country) & Q(service=obj.service)).first()

        # Create empty Stats object when no report for service/country in bd
        if not stats24h:
            stats24h = StatsReport24H()
            stats24h.id = 0
            stats24h.service = obj.service
            stats24h.country = obj.country
            stats24h = SerializerUtils.emptyStats24H(stats24h)

        return StatsReport24HSerializer(stats24h, many=False).data
