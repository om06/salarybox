from rest_framework import viewsets

from coordinates.permissions import IsGroupLeader
from coordinates.managers.points_data import PointsDataManager
from rest_framework.request import Request

from coordinates.utils import DefaultAPIResponse


class GroupDataViewSet(viewsets.ViewSet):
    permission_classes = [IsGroupLeader]

    def retrieve(self, request: Request, pk: str):
        group_code = pk
        manager = PointsDataManager(user=request.user)
        points_data = manager.get_group_members_data_points(group_code)
        return DefaultAPIResponse(points_data)
