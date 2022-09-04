from django.urls import include, re_path
from rest_framework import routers
from coordinates.views.points_data import PointsDataViewSet
from coordinates.views.group_data import GroupDataViewSet

router = routers.DefaultRouter()
router.register('points', PointsDataViewSet, basename='points')
router.register('group', GroupDataViewSet, basename='group')

urlpatterns = [
    re_path(r'^', include(router.urls,)),
]
