from .models import Notification,UserHaveNotification
from accounts.models import CustomUser
from rest_framework import serializers
from accounts import roles
# from management.models import SampleForm
from . import frontend_setting



class FromUSerNotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'full_name', 'phone', 'image', ]

# class UserHaveNotificationsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = UserHaveNotification
#         fields = ['id', 'is_read' ]    

class NotificationReadSerializer(serializers.ModelSerializer):  
    # from_notification = FromUSerNotificationSerializers()  
    is_read = serializers.SerializerMethodField()    
    class Meta:
        model = Notification
        fields = ['notification_message','id','created_date','path','is_read']
        # exclude = ['to_notification','updated_date','message_description','object_id','content_type','from_notification']

    def get_is_read(self,obj):
        user = self.context.get('request').user
        user_have_notify_obj = obj.user_have_notifications.all().filter(to_notification__in = [user])
        if user_have_notify_obj.exists():
            return user_have_notify_obj.first().is_read
        return False
    

class NotificationWriteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Notification
        fields = '__all__'


 