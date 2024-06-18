from django.db import models
from accounts.models import CustomUser

# Create your models heres.

class Resumes(models.Model):
    cv = models.FileField(upload_to='users/jobseeker/cv')
    user = models.ForeignKey(CustomUser,related_name = 'resumes',on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
