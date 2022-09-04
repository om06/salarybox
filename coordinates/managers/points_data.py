from collections import defaultdict

from coordinates.models import GroupLeader, PointsData
from coordinates.serializers.points_data import PointsDataValidateSerializer
from django.shortcuts import get_object_or_404


class PointsDataManager:
    def __init__(self, user):
        self.user = user

    def add_data_points(self, points: list):
        """
        Add points data for given user, taking points as list so that single as well as multiple points addition is
        supported by this function.
        """
        if not isinstance(points, list):
            return False, f"points data expected in list but found {type(points)}"
        for point in points:
            point['user_id'] = self.user.id

        serializer = PointsDataValidateSerializer(data=points, many=True)
        is_valid = serializer.is_valid()
        if not is_valid:
            return False, serializer._errors

        serializer.save()
        return True, "Successfully added points data"

    def add_points_via_csv(self):
        pass

    def get_user_data_points(self):
        """
        List all the points for a given user
        """
        return list(self.user.points_data.values('x', 'y'))

    def get_group_members_data_points(self, group_code):
        """
        Return the coordinates of all the users in the group with <group_code>
        """
        # TODO: Can we optimize this queries further, please check?
        group = get_object_or_404(GroupLeader, user=self.user, group__code=group_code).group
        points = PointsData.objects.filter(
            user__group_members__group__code=group.code).values('user__username', 'x', 'y')

        final_data = defaultdict(list)
        for data in points:
            final_data[data.pop('user__username')].append(data)
        return final_data
