from rest_framework import viewsets

from coordinates.permissions import IsGroupLeader
from rest_framework.request import Request


class GraphViewSet(viewsets.ViewSet):
    authentication_classes = [IsGroupLeader]

    def create(self, request: Request):
        pass

    def retrieve(self, request, pk):
        """
        To check status
        """
        pass