from rest_framework import serializers
from api.models import Service, CurrentStatus
from api.utils import SerializerUtils


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'slug', 'description', 'path', 'website', 'twitterUsername', 'countries')
        depth = 1


class DynamicFieldsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())

            # Error manage
            SerializerUtils.check_field_is_in_serializer(fields, existing, "ServiceSerializerFields")

            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ServiceSerializerFields(DynamicFieldsSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        depth = 1


class ServiceWithStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'slug', 'path',  'countries')

