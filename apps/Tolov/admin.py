from django.contrib import admin
from .models import ThresholdAutoPayment, ScheduledAutoPayment

# Register your models here.
admin.site.register([ThresholdAutoPayment, ScheduledAutoPayment])