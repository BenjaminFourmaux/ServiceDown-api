from rest_framework import serializers
from api.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('service', 'country', 'status.label')
