from django.db import models
import uuid
from django.utils.text import slugify
from company.models import Company
from professions.models import Profession

from jobutils.models import JobLevel,JobLocation,JobTiming


# Create your models here.

class JobCategory(models.Model):
    name = models.CharField(max_length = 250,unique = True)
    image = models.ImageField(upload_to='jobs/category/images',blank=True,null=True)
    is_popular = models.BooleanField(default = False)
    slug = models.CharField(max_length = 250,unique = True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Skills(models.Model):
    name = models.CharField(max_length = 150,unique = True)
    category = models.ForeignKey(JobCategory,on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Jobs(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 250,null=True,default='')
    position = models.ForeignKey(Profession,related_name="jobs",on_delete=models.PROTECT)
    level = models.ForeignKey(JobLevel, null = True, on_delete = models.SET_NULL)
    location = models.ForeignKey(JobLocation,null = True,on_delete = models.SET_NULL)
    required_number = models.PositiveIntegerField()
    description = models.TextField()
    timing = models.ForeignKey(JobTiming,null=True,on_delete = models.SET_NULL)
    salary_mode = models.CharField(max_length = 20, choices = (('Annually','annually'),('Hourly','hourly'),('Monthly','monthly')),default = 'monthly')
    min_salary = models.IntegerField(null = True)
    max_salary = models.IntegerField(null = True)
    category = models.ForeignKey(JobCategory,on_delete = models.PROTECT)
    company =  models.ForeignKey(Company,on_delete = models.CASCADE,related_name="jobs")
    is_active = models.BooleanField(default = True)
    status = models.CharField(max_length = 20, choices = (('pending','Pending'),('rejected','Rejected'),('approved','Approved')),default = 'pending')
    is_verified = models.BooleanField(default = False)

    image = models.ImageField(upload_to='jobs/images',null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    expiry_date = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.company.company_name)+"-"+str(self.title)
    
    @property
    def number_of_applicant(self):
        return self.job_seekers.all().count()
    
