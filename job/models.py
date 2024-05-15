from django.db import models
import uuid
from django.utils.text import slugify
from company.models import Company

# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length = 250,unique = True)
    image = models.ImageField(upload_to='jobs/category/images')
    is_popular = models.BooleanField(default = False)
    slug = models.CharField(max_length = 250,unique = True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type)
        super().save(*args, **kwargs)

class Skills(models.Model):
    name = models.CharField(max_length = 150)
    category = models.ForeignKey(JobCategory,on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Jobs(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 250,null=True,default='')
    position = models.CharField(max_length = 200)
    level = models.CharField(max_length = 50, choices = (('intern','Intern'),('junior','Junior'),('mid','Mid'),('senior','Senior'),('','')),default = '',null = True)
    required_number = models.PositiveIntegerField()
    description = models.TextField()
    timing = models.CharField(max_length = 20, choices = (('full_time','Full Time'),('part_time','Part Time'),('remote','Remote')),default = 'full_time')
    salary_mode = models.CharField(max_length = 20, choices = (('annually','annually'),('hourly','hourly'),('monthly','monthly')),default = 'monthly')
    min_salary = models.IntegerField(null = True)
    max_salary = models.IntegerField(null = True)
    category = models.ForeignKey(JobCategory,on_delete = models.PROTECT)
    company =  models.ForeignKey(Company,on_delete = models.CASCADE)
    is_active = models.BooleanField(default = True)
    is_verified = models.BooleanField(default = False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.company.company_name)+"-"+str(self.title)
