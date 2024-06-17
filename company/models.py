from django.db import models
import uuid
from django.utils.text import slugify
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.
class CompanyType(models.Model):
    type = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200,blank = True,unique = True)

    def __str__(self):
        return self.type
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type)
        super().save(*args, **kwargs)

class Company(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    company_name = models.CharField(max_length = 200)
    company_slug = models.CharField(max_length = 200,unique = True)
    type = models.ManyToManyField(CompanyType,related_name="companiess")
    mobile_number = models.CharField(max_length = 15)
    email = models.EmailField()
    company_logo = models.ImageField(upload_to='company/images',null=True,blank=True)
    company_banner = models.ImageField(upload_to='company/images',null=True,blank=True)
    about = models.TextField(null = True,blank = True)
    company_size = models.CharField(max_length = 350,null = True)
    website = models.URLField(max_length = 300,null = True)
    is_verified = models.BooleanField(default = False)
    owner = models.ForeignKey(CustomUser,on_delete = models.PROTECT,related_name="my_companies")
    location = models.CharField(max_length = 950,null  = True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.company_slug:
            self.company_slug = slugify(self.company_name)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)

    @property
    def total_active_job(self):
        return self.jobs.filter(is_active=True, is_verified=True, expiry_date__gte=timezone.now()).count()

