# Generated by Django 4.1 on 2022-09-03 20:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coordinates', '0003_rename_groupmembers_groupmember'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupleader',
            unique_together={('user', 'group')},
        ),
    ]