from django.urls import include, re_path
from rest_framework import routers
from coordinates.views.points_data import PointsDataViewSet

router = routers.DefaultRouter()
router.register('points', PointsDataViewSet, basename='points')

urlpatterns = [
    re_path(r'^', include(router.urls,)),
]
