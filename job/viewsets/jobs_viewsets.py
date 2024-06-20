from ..models import Jobs
from ..serializers.jobs_serializers import JobListPublicSerializer,JobListAdminSerializer,JobRetrievePublicSerializer,JobRetrieveAdminSerializer,JobWriteSerializers
from ..utilities.importbase import *
from ..utilities.permission import JobPermission
from accounts.models import roles
from rest_framework.decorators import action
from rest_framework.response import Response
from jobbookmark.models import JobsBookmark
from ..utilities.job_filter import JobFilter
from django.utils import timezone

from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
cache_time = 300 # 300 is 5 minute

class JobViewSets(viewsets.ModelViewSet):
    serializer_class = JobListPublicSerializer
    permission_classes = [JobPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Jobs.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['title','position__name','company__company_name','job_seekers__user__email','job_seekers__user__username']
    ordering_fields = ['id','created_date','position__name']
    filterset_class = JobFilter

 
    def get_queryset(self):
        user = self.request.user
        query = super().get_queryset()
        # return query
        if user.is_authenticated and user.role == roles.JOBSEEKER:
            query = query.filter(is_active = True).filter(expiry_date__gt=timezone.now())
        elif user.is_authenticated and user.role in [roles.ENTREPRENEUR,roles.ADMIN]:
            query = query.filter(company__owner = user)
        elif user.is_authenticated and user.role in [roles.ADMIN]:
            pass
        else:
            query = query.filter(is_active = True).filter(expiry_date__gt=timezone.now())
        return query.order_by('created_date')

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobWriteSerializers
        elif self.action in ['list']:
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                return JobListAdminSerializer
            else:
                return JobListPublicSerializer
        elif self.action in ['retrieve']:
            
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                return JobRetrieveAdminSerializer
            
            else:
                print(self.action," public retrieve",self.request.user.is_authenticated)
                return JobRetrievePublicSerializer
            
        return super().get_serializer_class()
    
    # @method_decorator(cache_page(cache_time,key_prefix="Job"))
    def list(self, request, *args, **kwargs):
        print("\n **************** this is job ")
        return super().list(request, *args, **kwargs)
    
 
    @action(detail=True, methods=['get'], name="SavedUnsavedJobs", url_path="job-save-unsave")
    def SavedUnsavedJobs(self, request, *args, **kwargs):
        obj = self.get_object()
        saved_data = JobsBookmark.objects.filter(user = self.request.user , job = obj)
        if saved_data.exists():
            saved_data.delete()
            return Response({'message':"job saved successfully"})
        else:
            JobsBookmark.objects.create(user = self.request.user,job = obj)
            return Response({'message':"job deleted successfully"})