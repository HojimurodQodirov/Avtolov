from django.contrib import admin
from .models import House, PlasticCard

# Register your models here.
admin.site.register([House, PlasticCard])