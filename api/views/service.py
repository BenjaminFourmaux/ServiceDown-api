from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models import Service
from api.serializers import ServiceSerializer, ServiceSerializerFields
from api.utils import ServiceNotFound


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects
    serializer_class = ServiceSerializer
    serializer_fields_class = ServiceSerializerFields

    def retrieve(self, request, *args, **kwargs):
        try:
            service = self.get_object()
        except:
            raise ServiceNotFound

        if 'fields' in request.GET:
            fields = request.GET.get('fields').split(',')

            output = self.serializer_fields_class(service, many=False, fields=tuple(fields))
        else:
            output = self.get_serializer(service, many=False)

        return Response(output.data, status=status.HTTP_200_OK)


