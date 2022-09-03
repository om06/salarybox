import uuid
from coordinates.models import CommonModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class GraphTask(CommonModel):
    user = models.ForeignKey(User, related_name="graph_tasks", on_delete=models.CASCADE)
    processed = models.BooleanField(default=False)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.user} - {self.reference_id} - {self.processed}"


class Graph(CommonModel):
    task = models.OneToOneField(GraphTask, related_name='graph', on_delete=models.PROTECT)
    result = models.CharField(max_length=200)  # Can be URL field if we are using some kind of cloud storage

    def __str__(self):
        return self.task.reference_id
