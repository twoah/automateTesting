from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response #api
from board.models import Scenario, Case
from django.db import IntegrityError
import os

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view #api
from rest_framework.response import Response #api

#리스트
def list(request):
    scenarios = Scenario.objects.all()
    return render(request, "board/list.html", {
        'scenarios': scenarios
    })
#새로 만들기
def create(request):
    if request.method == "GET" :
        return render(request, "board/create.html")
    
    #form Array
    form_gubuns = request.POST['gubuns[]']
    gubuns = form_gubuns.split(",")

    form_orders = request.POST['orders[]']
    orders = form_orders.split(",")

    form_ids = request.POST['ids[]']
    ids = form_ids.split(",")

    form_values = request.POST['values[]']
    values = form_values.split(",")
    
    #시나리오
    app_name = request.POST.get('app_name', None)
    use_yn = request.POST.get('use_yn', None)
    title = request.POST.get('title', None)
    description = request.POST.get('description',None)

    try :
        data = Scenario.objects.create(app_name = app_name, use_yn = use_yn, title = title, description = description)
        data.save()        
        for i in range(0, len(gubuns)) : 
            Case.objects.create(gubun=gubuns[i], order = orders[i], element_id = ids[i], element_value = values[i], scenario_id = data.id).save()
    except IntegrityError:
        print("data already exists.")
        return HttpResponse(status=500)
    return redirect('/list')


def detail(request, scenario_id):
    scenario = Scenario.objects.filter(id = scenario_id)[0]
    cases = Case.objects.filter(scenario_id = scenario_id).order_by('order')

    return render(request, "board/update.html", {   
        'scenario' : scenario, 
            'cases' : cases
    })
    
#수정 
def update(request):

    scenario_id = request.POST['scenario_id']
    #form Array
    form_case_ids = request.POST['case_ids[]']
    case_ids = form_case_ids.split(",")

    form_gubuns = request.POST['gubuns[]']
    gubuns = form_gubuns.split(",")

    form_orders = request.POST['orders[]']
    orders = form_orders.split(",")

    form_ids = request.POST['ids[]']
    ids = form_ids.split(",")

    form_values = request.POST['values[]']
    values = form_values.split(",")
    
    app_name = request.POST.get('app_name', None)
    use_yn = request.POST.get('use_yn')
    title = request.POST.get('title', None)
    description = request.POST.get('description',None)

    scenario = Scenario.objects.filter(id = scenario_id)
    scenario.update(title = title, description = description, use_yn = use_yn, app_name = app_name)

    for i in range(0, len(ids)) :
        if i < len(case_ids) : #업데이트
            case = Case.objects.filter(id = case_ids[i])
            case.update(gubun = gubuns[i], order = orders[i], element_id = ids[i], element_value = values[i])
        else : #추가 생성 
            data = Case.objects.create(scenario_id = scenario_id, gubun = gubuns[i], order = orders[i], element_id = ids[i], element_value = values[i])
            data.save()   
            
    return redirect('/list')  

#시나리오 및 케이스 삭제
def delete(request, scenario_id):
    data = Scenario.objects.filter(id=scenario_id)
    data.delete()

    cases = Case.objects.filter(scenario_id = scenario_id)
    cases.delete()

    return redirect('/list')