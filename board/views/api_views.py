from board.models import Scenario, Case, Device
from board.serializers import ScenarioSerializer, CaseSerializer, DeviceSerializer
from rest_framework.decorators import api_view #api
from rest_framework.response import Response #api

#시나리오 
@api_view(['GET'])
def getScenario(request, app_name):
    scenario = Scenario.objects.filter(app_name = app_name, use_yn = "y")
    serialized_scenario = ScenarioSerializer(scenario, many = True)
    return  Response(serialized_scenario.data)

#케이스
@api_view(['GET'])
def getCase(request, scenario_id): 
    case = Case.objects.filter(scenario_id = scenario_id)
    serialized_case = CaseSerializer(case, many = True)
    return Response(serialized_case.data)

#디바이스
@api_view(['GET'])
def getDevice(request, device_name):
    device = Device.objects.filter(device_name = device_name)
    serialized_device = DeviceSerializer(device, many = True)
    return Response(serialized_device.data)