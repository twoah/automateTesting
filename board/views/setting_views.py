from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response #api
from board.models import Scenario, Case, Device
from django.db import IntegrityError
import os

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view #api
from rest_framework.response import Response #api

#설정
def setting(request):

    devices = Device.objects.all()
    return render(request, "board/setting.html", {
        'devices' : devices
    });

def settingDetail(request, device_id): 
    if request.method == 'GET':
        device = Device.objects.filter(id = device_id)[0]
        return render(request, "board/setting_detail.html", {
            'device' : device
        });
    device = Device.objects.filter(id = device_id)
    device.update(app_name = request.POST['app_name'], app_version = request.POST['app_version'], 
                    device_os = request.POST['device_os'], device_name = request.POST['device_name'], 
                    platform_version = request.POST['platform_version'], app_activity = request.POST['app_activity'], 
                    app_file_name = request.POST['app_file_name'])

    devices = Device.objects.all()
    return render(request, "board/setting.html", {
            'devices' : devices
        });

def settingDelete(request, device_id):

    data = Device.objects.filter(id = device_id)
    data.delete()

    devices = Device.objects.all()
    return render(request, "board/setting.html", {
            'devices' : devices
        });


