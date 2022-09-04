from rest_framework import viewsets, status

from rest_framework.request import Request

from coordinates.managers import GraphManager
from coordinates.utils import DefaultAPIResponse


class GraphViewSet(viewsets.ViewSet):

    def create(self, request: Request):
        manager = GraphManager(user=request.user)
        response = manager.add_graph_task()
        return DefaultAPIResponse(response)

    def retrieve(self, request, pk):
        """
        To check status
        """
        manager = GraphManager(user=request.user)
        response = manager.get_graph_status(reference_id=pk)
        return DefaultAPIResponse(response)