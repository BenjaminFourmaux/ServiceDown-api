from rest_framework import serializers
from api.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'cname', 'description', 'path', 'website', 'twitterUsername', 'countries')
