from django.contrib import admin
from .models import Scenario, Case, Device

admin.site.register(Scenario)
admin.site.register(Case)
admin.site.register(Device)