from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Notification(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type','object_id')

    not_type = models.CharField(max_length=200,choices = (('sticky','Sticky'),('push','Push'),('admin_push','admin_push')),null=True,default="push")
    notification_type = models.CharField(max_length=200,null=True)

    notification_message = models.CharField(max_length=200,null=True)
    message_description = models.TextField(null=True)
    from_notification = models.ForeignKey(CustomUser,related_name="notifications",on_delete=models.CASCADE,null=True)
    path = models.CharField(max_length=1000,null=True)
    url = models.CharField(max_length=1000,null=True)

    to_notification = models.ManyToManyField(CustomUser,through="UserHaveNotification")

    created_date = models.DateTimeField(auto_now_add=True)  
    updated_date = models.DateTimeField(auto_now=True)


class UserHaveNotification(models.Model):
    to_notification = models.ForeignKey(CustomUser,related_name="user_have_notifications",on_delete = models.CASCADE)
    notification = models.ForeignKey(Notification,related_name="user_have_notifications",on_delete = models.CASCADE)
    is_read = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

