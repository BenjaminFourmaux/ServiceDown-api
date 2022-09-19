from rest_framework import serializers
from api.models import CurrentStatus


class CurrentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentStatus
        fields = ('service', 'country', 'status')
        depth = 1
