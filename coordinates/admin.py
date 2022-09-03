from coordinates.models import PointsData, UserGroup, GroupLeader, GroupMember, GraphTask, Graph
from django.contrib import admin

# Register your models here.
admin.site.register(GroupLeader)
admin.site.register(GroupMember)
admin.site.register(PointsData)
admin.site.register(UserGroup)
admin.site.register(Graph)
admin.site.register(GraphTask)
