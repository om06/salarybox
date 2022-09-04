import logging
import matplotlib.pyplot as plt
from celery import shared_task
from django.shortcuts import get_object_or_404

from coordinates.models import Graph
from coordinates.models.graph import GraphStatus


logger = logging.getLogger(__name__)


@shared_task()
def plot_graph(reference_id):
    logger.info(f"Task received: {reference_id}")
    graph_task = get_object_or_404(Graph, reference_id=reference_id)
    user = graph_task.user
    points = user.points_data.all()
    x_points = list(points.values_list('x', flat=True))
    y_points = list(points.values_list('y', flat=True))
    logger.info(f"[{reference_id}] x_points: {x_points} y_points: {y_points}")
    graph_task.update_status(GraphStatus.IN_PROGRESS)
    plt.scatter(x_points, y_points)
    path = f"uploads/{reference_id}.png"  # TODO: Fix this path
    plt.savefig(path)
    logger.info(f"[{reference_id}] Image generated")
    graph_task.result = path  # TODO: make this file field and save the file instance
    graph_task.update_status(GraphStatus.COMPLETED)
    logger.info(f"[{reference_id}] process completed")


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
        plot_graph.delay(reference_id)
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
