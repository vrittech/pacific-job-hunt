from ..models import Jobs
from ..serializers.jobs_serializers import JobListPublicSerializer,JobListAdminSerializer,JobRetrievePublicSerializer,JobRetrieveAdminSerializer,JobWriteSerializers
from ..utilities.importbase import *
from ..utilities.permission import JobPermission
from accounts.models import roles
from rest_framework.decorators import action
from rest_framework.response import Response
from jobbookmark.models import JobsBookmark
from ..utilities.job_filter import JobFilter

class JobViewSets(viewsets.ModelViewSet):
    serializer_class = JobListPublicSerializer
    permission_classes = [JobPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Jobs.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['title','position','company__company_name']
    ordering_fields = ['id']
    filterset_class = JobFilter

    # filterset_fields = {
    #     'category':['exact'], #multiple
    #     'min_salary': ['exact', 'gte', 'lte'],
    #     'level':['exact'],
    #     'location':['exact'],#multiple
    #     'timing':['exact'], #multiple
    #     'salary_mode':['exact'],
    #     'company__location':['icontains']

    # }


    def get_queryset(self):
        return super().get_queryset()

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
                print(self.action)
                return JobRetrieveAdminSerializer
            
            else:
                print(self.action," public retrieve",self.request.user.is_authenticated)
                return JobRetrievePublicSerializer
            
        return super().get_serializer_class()
    
 
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