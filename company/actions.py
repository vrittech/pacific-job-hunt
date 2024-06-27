from django.db.models.signals import pre_save,post_save , pre_delete
from django.dispatch import receiver
from .models import CustomUser
from notification.handle_notification import NotificationHandler


@receiver(pre_save, sender=CustomUser)
def CompanyPreSave(sender, instance, **kwargs):
    if not instance.pk:
        NotificationHandler(instance,"company_register")