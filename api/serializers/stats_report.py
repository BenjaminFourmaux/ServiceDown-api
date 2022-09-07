from rest_framework import serializers
from api.models import StatsReport1H, StatsReport24H


class StatsReport1HSerializer(serializers.ModelSerializer):
    intervals = serializers.SerializerMethodField()

    class Meta:
        model = StatsReport1H
        fields = (
            'id',
            'service',
            'country',
            'intervals',
            'totalReport',
        )

    @staticmethod
    def get_intervals(obj):
        return [
            obj.interval60mins,
            obj.interval55mins,
            obj.interval50mins,
            obj.interval45mins,
            obj.interval40mins,
            obj.interval35mins,
            obj.interval30mins,
            obj.interval25mins,
            obj.interval20mins,
            obj.interval15mins,
            obj.interval10mins,
            obj.interval5mins,
        ]


class StatsReport24HSerializer(serializers.ModelSerializer):
    intervals = serializers.SerializerMethodField()

    class Meta:
        model = StatsReport24H
        fields = (
            'id',
            'service',
            'country',
            'intervals',
            'totalReport',
        )

    @staticmethod
    def get_intervals(obj):
        return [
            obj.interval24hours,
            obj.interval23hours,
            obj.interval22hours,
            obj.interval21hours,
            obj.interval20hours,
            obj.interval19hours,
            obj.interval18hours,
            obj.interval17hours,
            obj.interval16hours,
            obj.interval15hours,
            obj.interval14hours,
            obj.interval13hours,
            obj.interval12hours,
            obj.interval11hours,
            obj.interval10hours,
            obj.interval9hours,
            obj.interval8hours,
            obj.interval7hours,
            obj.interval6hours,
            obj.interval5hours,
            obj.interval4hours,
            obj.interval3hours,
            obj.interval2hours,
            obj.interval1hours,
        ]
