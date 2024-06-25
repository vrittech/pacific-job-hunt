from django.db import models
from accounts.models import CustomUser

# Create your models here.
class EducationLevel(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Education(models.Model):
    college = models.CharField(max_length = 2000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="educations")
    degree_name = models.CharField(max_length = 1000)  # in years
    education_level = models.ForeignKey(EducationLevel,on_delete = models.SET_NULL,null = True)
    joined_date = models.DateField(null = True)
    end_date  = models.DateField(null = True)
    is_currently = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True)
