from coordinates.models import CommonModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class PointsData(CommonModel):
    user = models.ForeignKey(User, related_name="points", on_delete=models.PROTECT)
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username}: {self.x}, {self.y}"
