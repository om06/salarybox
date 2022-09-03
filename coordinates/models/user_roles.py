from coordinates.models import CommonModel
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserGroup(CommonModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)  # Generally it will be the slug of the name

    def __str__(self):
        return self.name


class GroupMembers(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group.name} - {self.user.username}"


class GroupLeader(CommonModel):
    """
    This information could have been stored in GroupMembers table using one extra flag is_leader, but with every row
    it will have this information and in the long run will increase the size of the db and again if we want to store
    more information of GroupLeader we can do it here without migrating the data. This is the best choice keeping the
    scalability in mind.
    """
    user = models.ForeignKey(User, related_name='group_leaders', on_delete=models.CASCADE)
    group = models.ForeignKey(UserGroup, related_name='group_leaders', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group.name} - {self.user.username}"
