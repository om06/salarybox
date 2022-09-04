from django.urls import include, re_path
from rest_framework import routers
from coordinates.views import PointsDataViewSet, GroupDataViewSet, GraphViewSet

router = routers.DefaultRouter()
router.register('points', PointsDataViewSet, basename='points')
router.register('group', GroupDataViewSet, basename='group')
router.register('graph', GraphViewSet, basename='graph')

urlpatterns = [
    re_path(r'^', include(router.urls,)),
]
