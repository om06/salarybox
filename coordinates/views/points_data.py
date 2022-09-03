from coordinates.managers import PointsDataManager
from rest_framework import status, viewsets
from rest_framework.request import Request
from coordinates.utils import DefaultAPIResponse, ErrorAPIResponse


class PointsDataViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        manager = PointsDataManager(user=request.user)
        data = manager.get_user_data_points()
        return DefaultAPIResponse(data)

    def create(self, request: Request):
        points_data = request.data
        if isinstance(points_data, dict):
            points_data = [points_data]
        manager = PointsDataManager(user=request.user)
        added, message = manager.add_data_points(points_data)

        if not added:
            return ErrorAPIResponse(message)
        return DefaultAPIResponse(message, http_status=status.HTTP_201_CREATED)



