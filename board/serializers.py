from django.core import serializers
from rest_framework import serializers
from .models import Scenario, Case, Device

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Scenario
        fields = ['id', 'title', 'description', 'app_name', 'use_yn']
    id = serializers.CharField(max_length = 100)
    title = serializers.CharField(max_length = 100)
    description = serializers.CharField(max_length = 100)
    app_name = serializers.CharField(max_length = 100)
    use_yn = serializers.CharField(max_length = 100)


class CaseSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Case
        fields = ['id', 'gubun', 'element_id', 'element_value','try_count','scenario_id','order']
    id = serializers.CharField(max_length = 100)
    gubun =  serializers.CharField(max_length = 1000)
    element_id =  serializers.CharField(max_length = 1000)
    element_value =  serializers.CharField(max_length = 1000)
    try_count = serializers.IntegerField()
    scenario_id = serializers.CharField(max_length = 1000)
    order = serializers.IntegerField()

class DeviceSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Device
        fields = ['id', 'title', 'device_name', 'device_os', 'platform_version', 'app_name', 'app_activity', 'app_file_name', 'app_version']
    id = serializers.CharField(max_length = 100)
    title = serializers.CharField(max_length = 100)
    device_name =  serializers.CharField(max_length = 1000)
    device_os =  serializers.CharField(max_length = 1000)
    platform_version =  serializers.CharField(max_length = 1000)
    app_name = serializers.CharField(max_length = 1000)
    app_activity = serializers.CharField(max_length = 1000)
    app_file_name = serializers.CharField(max_length = 1000)
    app_version = serializers.CharField(max_length = 1000)
