from django.db.models import Q
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from api.models import Service
from api.serializers import ServiceSerializer
from api.utils import MissingQueryParameter


class SearchViewSet(viewsets.ModelViewSet):

    @action(methods=['GET'], detail=False, url_path='service', url_name='search service')
    def search_services(self, request, *args, **kwargs):
        if 'q' in request.GET:
            services = Service.objects.filter(name__istartswith=request.GET['q'])
            serializer = ServiceSerializer(services, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise MissingQueryParameter
