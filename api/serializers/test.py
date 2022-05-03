from rest_framework import serializers
from api.models.test import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'label')