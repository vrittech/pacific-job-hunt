from django.db.models.signals import pre_save,post_save , pre_delete
from django.dispatch import receiver
from .models import CustomUser
from notification.handle_notification import NotificationHandler


@receiver(pre_save, sender=CustomUser)
def CustomUserPreSave(sender, instance, **kwargs):
    if instance.pk:
        if instance.password != CustomUser.objects.get(id = instance.id).password:
            NotificationHandler(instance,"password_changed")