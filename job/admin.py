from django.contrib import admin
from .models import JobCategory,Jobs,Skills,Profession
# Register your models here.
admin.site.register([JobCategory,Jobs,Skills,Profession])
