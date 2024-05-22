from django.db import models
from django.utils.text import slugify

# Create your models here.
class Profession(models.Model):
    name = models.CharField(max_length = 250,unique = True)
    image = models.ImageField(upload_to='profession/images',null = True,blank = True)
    slug = models.CharField(max_length = 250,unique = True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)