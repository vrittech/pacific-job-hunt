from django.db.models.signals import pre_save,post_save , pre_delete
from django.dispatch import receiver
from .models import Company
from notification.handle_notification import NotificationHandler


@receiver(pre_save, sender=Company)
def CompanyPreSave(sender, instance, **kwargs):
    if not instance.pk:
        NotificationHandler(instance,"company_register")