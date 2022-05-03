from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Test
from api.serializers import TestSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.object
    serializer_class = TestSerializer

    @action(methods=['GET'], detail=False, url_path='ping', url_name='ping pong')
    def ping_pong(self, request, pk=None):
        return Response('pong', status=status.HTTP_200_OK)
