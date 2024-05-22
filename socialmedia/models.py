from django.db import models
from accounts.models import CustomUser

# Create your models here.
class SocialMedia(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="social_media/images")

class MySocialMedia(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="social_media")
    url = models.URLField()
    social_media = models.ForeignKey(SocialMedia,related_name="jobseeker_socialmedia",on_delete=models.CASCADE)

    