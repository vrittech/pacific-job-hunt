
from rest_framework import viewsets
from . models import Notification,UserHaveNotification
from rest_framework import status
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import PageNumberPagination
from rest_framework.response import Response
from .serializer import NotificationWriteSerializer,NotificationReadSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .custom_filters import CustomFilter
from .custompermission import NotificationPermission
from django.http import  HttpResponse
from datetime import date
from rest_framework.decorators import action

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
cache_time = 300 # 300 is 5 minutes
from accounts.models import CustomUser
from .handle_notification import NotificationHandler

from rest_framework.generics import views
from .seriaizers.push_notification_serializer  import PushNotificationSerializers_without_id#PushNotificationSerializers
# from products.models import Product
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class NotificationViewSet(viewsets.ModelViewSet):

    queryset = Notification.objects.all().order_by("-created_date")
    serializer_class = NotificationReadSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['notification_type']
    filterset_class = CustomFilter
    search_fields = ['notification_type']


    # authentication_classes = [JWTAuthentication]
    permission_classes = [NotificationPermission,IsAuthenticated]
    
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            query = Notification.objects.filter(to_notification__in = [user])  
            user_have_notifications_obj = list(UserHaveNotification.objects.all().filter(is_active = True).values_list('notification_id',flat = True))
        else:
            query = Notification.objects.none()    
        return query.filter().order_by("-created_date")
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return NotificationWriteSerializer
        return super().get_serializer_class()
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response
    
    @action(detail=False, methods=['get'], name="notificationCount", url_path="notification-count")
    def notificationCount(self, request):
        notification_obj = list(self.get_queryset().values_list('id',flat=True))
        user_have_notifications = UserHaveNotification.objects.all().filter(notification_id__in = notification_obj).filter(to_notification__in = [self.request.user])
        data  = {
            'unread_notification':user_have_notifications.filter(is_read = False).count(),
            'read_notification':user_have_notifications.filter(is_read = True).count(),
            'total_notification':user_have_notifications.count()
        }
        print(data)
        return Response({"message":data}, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'], name="allReadNotification", url_path="mark-as-all-read")
    def allReadNotification(self, request):
        marks_notification_ids = request.data.get('marks_notification_ids')
        print(type(marks_notification_ids),marks_notification_ids," mar as read")
        notification_obj = self.get_queryset()
        
        if marks_notification_ids:
            # notification_obj = notification_obj.filter(id__in = marks_notification_ids)
            notification_obj = UserHaveNotification.objects.filter(notification_id__in = marks_notification_ids,to_notification__in = [self.request.user])
            print(notification_obj," notification_obj")
        else:
            notification_obj  = UserHaveNotification.objects.filter(notification_id__in = list(notification_obj.values_list('id',flat=True)),to_notification__in = [self.request.user])

        notification_obj.update(is_read = True)

        return Response({"message":"mark as all read completed"}, status=status.HTTP_201_CREATED)
    

    @action(detail=False, methods=['post'], name="allClearNotification", url_path="mark-as-clear")
    def allClearNotification(self, request):
        marks_notification_ids = request.data.get('marks_notification_ids')
        notification_obj = self.get_queryset()
        
        if marks_notification_ids:
            # notification_obj = notification_obj.filter(id__in = marks_notification_ids)
            notification_obj = UserHaveNotification.objects.filter(notification_id__in = marks_notification_ids,to_notification__in = [self.request.user])
        else:
            notification_obj  = UserHaveNotification.objects.filter(notification_id__in = list(notification_obj.values_list('id',flat=True)),to_notification__in = [self.request.user])

        notification_obj.update(is_active = False)

        return Response({"message":"mark as clear notification"}, status=status.HTTP_201_CREATED)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the new object to the database
        self.perform_create(serializer)

        # Create a custom response
        response_data = {
            "message": "Notification created successfully",
            "data": serializer.data
        }

        # Return the custom response
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Save the updated object to the database
        self.perform_update(serializer)

        # Create a custom response
        response_data = {
            "message": "Notification updated successfully",
            "data": serializer.data
        }

        # Return the custom response
        return Response(response_data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Perform the default delete logic
        self.perform_destroy(instance)

        # Create a custom response
        response_data = {
            "message": "Notification category deleted successfully"
        }

        # Return the custom response
        return Response(response_data)

def birthdayAnniversaryNotification(request):
    today_date = date.today()
    users_with_birthday = CustomUser.objects.filter(dob__month=today_date.month, dob__day=today_date.day)
    users_with_anniversary = CustomUser.objects.filter(created_date__month=today_date.month, created_date__day=today_date.day)
    
    for user in users_with_birthday:
        print(f"Today is the birthday of {user.username}")
        NotificationHandler(user,request,"BirthDay",'CustomUser')
    
    for user in users_with_anniversary:
        print(f"Today is the anneversary of {user.created_date}")
        NotificationHandler(user,request,"Anniversary",'CustomUser')

    return HttpResponse("sent notification completed")

class PushNotificationView(views.APIView):
    def post(self,request,*args,**kwargs):
        if request.data.get('type') in ['product_push_notification','collection_push_notification']:
            serializer = PushNotificationSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            type = serializer.validated_data.get('type')
            file = serializer.validated_data.get('file')
            title = serializer.validated_data.get('title')
            url = serializer.validated_data.get('url')
            instance =  serializer.validated_data.get('id')
            message = serializer.validated_data.get('message')
        
            # if type == "product_push_notification":
            NotificationHandler(instance,type,message,title,file,url)

        else:
            serializer = PushNotificationSerializers_without_id(data=request.data)
            serializer.is_valid(raise_exception=True)
            type = serializer.validated_data.get('type')
            file = serializer.validated_data.get('file')
            title = serializer.validated_data.get('title')
            url = serializer.validated_data.get('url')
            path = serializer.validated_data.get('path')
            instance =  Product.objects.all().first()
            message = serializer.validated_data.get('message')
        
            # if type == "product_push_notification":
            NotificationHandler(instance,type,message,title,file,url,path)

        return Response({'status': 'Notification received'})
    
