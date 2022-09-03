from coordinates.models import PointsData, UserGroup, GroupLeader, GroupMembers
from django.contrib import admin

# Register your models here.
admin.site.register(GroupLeader)
admin.site.register(GroupMembers)
admin.site.register(PointsData)
admin.site.register(UserGroup)
