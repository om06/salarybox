from coordinates.managers import PointsDataManager
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response


class PointsDataViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        return Response({})

    def create(self, request: Request):
        points_data = request.data
        if isinstance(points_data, dict):
            points_data = [points_data]
        manager = PointsDataManager(user=request.user)
        added, message = manager.add_data_points(points_data)

        if not added:
            return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': message}, status=status.HTTP_201_CREATED)



