from coordinates.managers.points_data import PointsDataManager
from coordinates.utils import DefaultAPIResponse
from rest_framework import status, viewsets
from rest_framework.request import Request


class LoadFileViewSet(viewsets.ViewSet):

    def create(self, request: Request):
        manager = PointsDataManager(user=request.user)
        response = manager.add_points_via_csv(request.data)
        return DefaultAPIResponse(response, http_status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        reference_id = pk
        manager = PointsDataManager(user=request.user)
        response = manager.get_file_status(reference_id)
        return DefaultAPIResponse(response)

