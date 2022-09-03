from coordinates.models import PointsData
from rest_framework import serializers


class PointsDataValidateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(min_value=1)

    class Meta:
        model = PointsData
        fields = ('x', 'y', 'user_id')
