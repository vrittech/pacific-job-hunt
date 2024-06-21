from django.contrib import admin
from .models import Notification,UserHaveNotification

# Register your models here.

class UserHaveNotificationInline(admin.TabularInline):
    model = UserHaveNotification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    inlines = [UserHaveNotificationInline]

    list_display = ['notification_message','created_date']

