from coordinates.models import PointsData
from coordinates.serializers.points_data import PointsDataValidateSerializer


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
        pass
