from django.contrib import admin
from .models import JobSeeker,JobsApply,JobSeekerHaveSkills

admin.site.register([JobSeeker,JobsApply,JobSeekerHaveSkills])
