# Generated by Django 4.1 on 2022-09-04 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coordinates', '0008_remove_graphtask_processed_graphtask_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Graph',
        ),
    ]
