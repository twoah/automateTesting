# Generated by Django 3.2.4 on 2021-09-03 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_remove_scenario_department_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scenario',
            old_name='detail',
            new_name='description',
        ),
    ]
