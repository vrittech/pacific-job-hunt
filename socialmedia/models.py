from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="social_media/images")
    