from rest_framework import viewsets

from coordinates.permissions import IsGroupLeader
from rest_framework.request import Request


class GroupDataViewSet(viewsets.ViewSet):
    authentication_classes = [IsGroupLeader]

    def retrieve(self, request: Request, pk: str):
        pass