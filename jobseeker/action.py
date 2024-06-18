from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import ProfessionalInformation
from resumes.models import Resumes


@receiver(pre_save, sender=ProfessionalInformation)
def ProfessionalInformation_pre_save_handler(sender, instance, **kwargs):
    if instance.cv:
        Resumes.objects.create(cv = instance.cv,user = instance.user)
