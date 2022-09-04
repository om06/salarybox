import csv
import io
import logging
from celery import shared_task
from collections import defaultdict

from coordinates.models import GroupLeader, PointsData, PointsFile
from coordinates.models.points_data import FileStatus
from coordinates.serializers import FileUploadSerializer
from coordinates.serializers.points_data import PointsDataValidateSerializer
from django.shortcuts import get_object_or_404


logger = logging.getLogger(__name__)


@shared_task()
def save_csv_file_task(reference_id):
    # TODO: This might raise exception, handle it
    logger.info(f"[{reference_id}] File task: Initiated")
    file_task = PointsFile.objects.get(reference_id=reference_id)
    file_task.update_status(FileStatus.IN_PROGRESS)
    file = file_task.file
    decoded_file = file.read().decode()
    io_string = io.StringIO(decoded_file)
    reader = csv.reader(io_string)
    logger.info(f"[{reference_id}] File task: Decoded file")

    rows_data = []
    for cnt, row in enumerate(reader, start=0):
        if cnt == 0:
            continue  # This is header row and we can ignore this
        data = {
            'x': row[0],
            'y': row[1]
        }
        rows_data.append(data)

    manager = PointsDataManager(user=file_task.user)
    added, message = manager.add_data_points(rows_data)
    if not added:
        logger.info(f"[{reference_id}] File task: Failed - {message}")
        file_task.update_status(FileStatus.FAILED)
    else:
        logger.info(f"[{reference_id}] File task: Completed")
        file_task.update_status(FileStatus.COMPLETED)
    file_task.message = message
    file_task.save()


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

    def add_points_via_csv(self, request_data):
        serializer = FileUploadSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        file_task = PointsFile.objects.create(user=self.user, file=file)
        save_csv_file_task.delay(file_task.reference_id)
        return {
            "reference_id": file_task.reference_id.hex,
            "message": f"File queued for further processing"
        }

    def get_file_status(self, reference_id):
        """
        Return the status of file task
        """
        file_task = get_object_or_404(PointsFile, reference_id=reference_id, user=self.user)
        return {
            "status": file_task.status,
            "message": file_task.message
        }

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
