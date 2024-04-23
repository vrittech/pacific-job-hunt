from django.contrib import admin
from .models import JobSeeker,JobsApply

admin.site.register([JobSeeker,JobsApply])
