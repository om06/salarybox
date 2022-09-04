import uuid
from coordinates.models import CommonModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class GraphStatus:
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

    CHOICES = (
        (PENDING, "Pending"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed")
    )


class Graph(CommonModel):
    user = models.ForeignKey(User, related_name="graph_tasks", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=GraphStatus.CHOICES, default=GraphStatus.PENDING)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False)
    result = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.reference_id} - {self.status}"

    def update_status(self, status):
        self.status = status
        self.save()
