from django.urls import path 
from . import views
from .views import api_views, crud_views, setting_views

app_name = 'board' 
urlpatterns = [ 
    path('', crud_views.list), 
    path('create', crud_views.create, name="create"),     
    path('update', crud_views.update, name="update"),  
    path('detail/<str:scenario_id>', crud_views.detail, name="detail"),    
    path('delete/<str:scenario_id>', crud_views.delete, name="delete"),    
    path('list', crud_views.list, name="list"),     
    path('setting', setting_views.setting, name="setting"),   
    path('setting/<str:device_id>', setting_views.settingDetail, name="settingDetail"),   
    path('setting/<str:device_id>', setting_views.settingDetail, name="settingDetail"),   
    path('setting/<str:device_id>/delete', setting_views.settingDelete, name="settingDelete"),    
    path('get/scenario/<str:app_name>', api_views.getScenario, name ="getScenario"),
    path('get/case/<str:scenario_id>', api_views.getCase, name = "getCase"),
    path('get/device/<str:device_name>', api_views.getDevice, name = "getDevice")
]