import uuid

from coordinates.models import CommonModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class FileStatus:
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    FAILED = "failed"

    CHOICES = (
        (PENDING, "Pending"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
        (FAILED, "Failed")
    )


class PointsData(CommonModel):
    user = models.ForeignKey(User, related_name="points_data", on_delete=models.PROTECT)
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username}: {self.x}, {self.y}"


def content_file_name(instance, filename):
    return '/'.join(['uploads', instance.user.username, f"{instance.reference_id.hex}-{filename}"])


class PointsFile(CommonModel):
    """
    Model to store the CSV file data
    """
    user = models.ForeignKey(User, related_name="points_file", on_delete=models.CASCADE)
    file = models.FileField(upload_to=content_file_name)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=20, choices=FileStatus.CHOICES, default=FileStatus.PENDING)
    message = models.TextField()

    def __str__(self):
        return f"{self.reference_id} - {self.status}"

    def update_status(self, status):
        self.status = status
        self.save()
