from django.db import models
from django.utils import timezone
import uuid

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(max_length=1000, null=True, blank=True)
    app_name =  models.CharField(max_length=1000, null=True, blank=True)
    app_version =  models.CharField(max_length=1000, null=True, blank=True)
    app_file_name = models.CharField(max_length=1000, null=True, blank=True)
    app_activity =  models.CharField(max_length=1000, null=True, blank=True)
    device_name =  models.CharField(max_length=1000, null=True, blank=True)
    device_os =  models.CharField(max_length=1000, null=True, blank=True)
    platform_version =  models.CharField(max_length=1000, null=True, blank=True)
    
class Scenario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    app_name = models.CharField(max_length=1000, null=True)
    use_yn = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)

class Case(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gubun = models.CharField(max_length=10000, null=True)
    element_id = models.CharField(max_length=1000, null=True)
    element_value = models.CharField(max_length=1000, null=True)
    try_count = models.IntegerField(default=0, null=True)
    scenario_id = models.CharField(max_length=1000, null=True)
    order = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)