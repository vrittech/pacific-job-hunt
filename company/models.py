from django.db import models
import uuid
from django.utils.text import slugify
from accounts.models import CustomUser

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
    type = models.ForeignKey(CompanyType,null = True , on_delete = models.PROTECT)
    mobile_number = models.CharField(max_length = 15)
    email = models.EmailField()
    company_logo = models.ImageField(upload_to='company/images')
    description = models.TextField(null = True,blank = True)
    company_size = models.CharField(max_length = 350)
    website = models.URLField(null = True,max_length = 300)
    is_verified = models.BooleanField(default = False)
    owner = models.ForeignKey(CustomUser,on_delete = models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.company_slug:
            self.company_slug = slugify(self.Company_name)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)

