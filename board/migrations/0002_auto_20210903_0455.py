# Generated by Django 3.2.4 on 2021-09-03 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='element_id',
            new_name='element_click_id',
        ),
        migrations.AddField(
            model_name='case',
            name='element_input',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='element_xpath',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='gubun',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='order',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='try_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='scenario',
            name='app_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='scenario',
            name='department_id',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
