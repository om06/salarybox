from django.shortcuts import get_object_or_404

from coordinates.models import Graph
from coordinates.models.graph import GraphStatus


class GraphManager:
    def __init__(self, user):
        self.user = user

    def add_graph_task(self):
        """
        Check whether user already have a task which is in pending status if yes than return its reference id otherwise
        add new task and return its reference id.
        """
        tasks = self.user.graph_tasks.filter(status=GraphStatus.PENDING)
        if tasks.exists():
            reference_id = tasks.last().reference_id.hex
            created = False
        else:
            task = self.user.graph_tasks.create()
            reference_id = task.reference_id.hex
            created = True
        response = {
            "created": created,
            "reference_id": reference_id
        }
        return response

    def get_graph_status(self, reference_id):
        task = get_object_or_404(Graph, user=self.user, reference_id=reference_id)
        response = {
            "status": task.status,
            "result": task.result
        }

        return response
