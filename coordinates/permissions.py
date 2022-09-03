from rest_framework import permissions, status
from rest_framework.exceptions import APIException


class Forbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = 'forbidden'

    def __init__(self, message):
        self.default_detail = message
        self.detail = message


class IsGroupLeader(permissions.BasePermission):
    message = ""

    def has_permission(self, request, view):
        group_code = request.data.get('group_code')
        group_exists = request.user.group_leaders.filter(group__code=group_code).exists()
        if not group_exists:
            # TODO: Check whether User is active or not
            message = f"{request.user.username} is not a leader of {group_code}"
            raise Forbidden(message)
        return True