
from accounts.models import CustomUser
from .models import Notification
from .serializer import NotificationWriteSerializer
from rest_framework import status
from . import frontend_setting
from . import mapping_notification_type
# from emailmanagement.email_sender import ESendMail
from accounts import roles
from django.db.models import Q
# Assuming you have the necessary imports
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from .mapping_notification_type import mapping
# from .one_signals import sendNotificationToOneSignals

from .mails.notification_mail import sendMail

def NotificationHandler(instance,method,request = None):

    if method == 'password_changed':
        to_notification = [instance.id]
        from_notification = instance.id
        path = "#"
        notification_message = mapping.get(method).get('admin_message').format(username=instance.username,user_id = instance.id)
        user_messaage = ''
        is_read = False
        group_notification = '..'

    elif method == 'job_':
        to_notification = [instance.user.id]
        from_notification = instance.user.id
        path = mapping.get(method).get('path').format(order_id=instance.id)
        notification_message = mapping.get(method).get('admin_message').format(order_id=instance.id)
        user_messaage = mapping.get(method).get('user_message').format(username=instance.username,user_id = instance.id)
        is_read = False
        group_notification = '..'

    elif method == 'collection_push_notification':
        to_notification = CustomUser.objects.all().values_list('id',flat=True)
        from_notification = CustomUser.objects.filter(Q(role = roles.ADMIN) | Q(role = roles.SUPER_ADMIN)).first().id
        path = mapping.get(method).get('path').format(id=instance.id)
        notification_message = ''
        user_messaage = ''
        is_read = False
        group_notification = '..'
        

    notification_data = {
        "notification_message": notification_message,
        "path": path,
        "from_notification": from_notification,
        "is_read": is_read,
        "group_notification": 'USER_ADMIN',
        "to_notification": to_notification,
        'object_id':instance.id,
        'content_object':instance,
        'content_type':ContentType.objects.get_for_model(instance).id,
        'notification_type':method,
    }


    try:
        serializer = save_notification(notification_data)
        #sendNotificationToOneSignals(notification_data,file = serializer.data.get('file'))
        #sendMail(notification_data)
        return True
    except:
        print("error in notification")

def save_notification(notification_data):
    serializer = NotificationWriteSerializer(data=notification_data)
    serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    instance.to_notification.set(notification_data['to_notification'])
    return True


