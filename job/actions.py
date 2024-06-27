from django.db.models.signals import pre_save,post_save , pre_delete
from django.dispatch import receiver
from .models import Jobs
from notification.handle_notification import NotificationHandler


@receiver(pre_save, sender=Jobs)
def JobPreSave(sender, instance, **kwargs):
    if not instance.pk:
        NotificationHandler(instance,"post_jobs")
