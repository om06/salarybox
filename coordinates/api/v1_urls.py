from django.urls import include, re_path
from rest_framework import routers
from coordinates.views import GraphViewSet, GroupDataViewSet, LoadFileViewSet, PointsDataViewSet

router = routers.DefaultRouter()
router.register('points', PointsDataViewSet, basename='points')
router.register('group', GroupDataViewSet, basename='group')
router.register('graph', GraphViewSet, basename='graph')
router.register('csv', LoadFileViewSet, basename='csv')

urlpatterns = [
    re_path(r'^', include(router.urls,))
]
