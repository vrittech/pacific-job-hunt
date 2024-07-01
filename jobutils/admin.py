from django.contrib import admin
from .models import JobLevel,JobLocation,JobTiming

# Register your models here.
admin.site.register([JobLevel,JobLocation,JobTiming])