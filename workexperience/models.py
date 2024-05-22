from django.db import models
from accounts.models import CustomUser
from job.models import JobCategory

# Create your models here.
class WorkExperience(models.Model):
    designation = models.CharField(max_length = 2000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="work_experience")
    experience = models.PositiveIntegerField()  # in years
    company_name  = models.CharField(max_length = 1500)
    designation = models.CharField(max_length = 1000)
    job_categories = models.ForeignKey(JobCategory,related_name = "work_experience",on_delete = models.SET_NULL,null = True)
    joined_date = models.DateField(null = True)
    end_date  = models.DateField(null = True)
    still_work = models.BooleanField(default = False)
