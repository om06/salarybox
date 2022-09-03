from coordinates.models import PointsData
from coordinates.serializers.points_data import PointsDataValidateSerializer


class PointsDataManager:
    def __init__(self, user):
        self.user = user

    def add_data_points(self, points: list):
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
        pass

    def get_group_members_data_points(self, group_code):
        pass
