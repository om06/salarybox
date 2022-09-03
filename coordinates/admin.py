from coordinates.models import PointsData, UserGroup, GroupLeader, GroupMember
from django.contrib import admin

# Register your models here.
admin.site.register(GroupLeader)
admin.site.register(GroupMember)
admin.site.register(PointsData)
admin.site.register(UserGroup)
