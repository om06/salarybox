# Generated by Django 4.1 on 2022-09-04 18:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coordinates', '0009_delete_graph'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GraphTask',
            new_name='Graph',
        ),
    ]
