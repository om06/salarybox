from rest_framework import viewsets
from rest_framework.response import Response


class PointsDataViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({})

    def create(self, request):
        pass
