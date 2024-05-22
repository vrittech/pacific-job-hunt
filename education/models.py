from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Education(models.Model):
    college = models.CharField(max_length = 2000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="educations")
    degree_name = models.CharField(max_length = 1000)  # in years
    company_name  = models.CharField(max_length = 1500)
    education_level = models.CharField(max_length = 1000)
    joined_date = models.DateField(null = True)
    end_date  = models.DateField(null = True)
