from ..models import JobsApply
from ..serializers.jobseeker_have_jobs_serializers import (
    JobsApplyPublicListSerializers,JobsApplyPublicRetrieveSerializers,
    JobsApplyAdminListSerializers,JobsApplyAdminRetrieveSerializers,
    getJobSeekers_JobsApplyAdminListReadSerializers,
    JobsApplyWriteSerializers
    )

from ..utilities.importbase import *
from accounts import roles
from rest_framework.decorators import action

class JobSeekerHaveJobsViewSets(viewsets.ModelViewSet):
    serializer_class = JobsApplyPublicListSerializers
    permission_classes = [AdminViewSetsPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobsApply.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    filterset_fields = {
        'user':['exact'],
        'job':['exact'],
    }

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobsApplyWriteSerializers
        elif self.action in ['jobSeekers']:
            return getJobSeekers_JobsApplyAdminListReadSerializers
        elif self.action in ['list']:
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                return JobsApplyAdminListSerializers
            else:
                return JobsApplyPublicListSerializers
        elif self.action in ['retrieve']:
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                print(self.action)
                return JobsApplyAdminRetrieveSerializers
            else:
                print(self.action," public retrieve",self.request.user.is_authenticated)
                return JobsApplyPublicRetrieveSerializers
            
        return super().get_serializer_class()
    
    @action(detail=False, methods=['get'], name="jobSeekers", url_path="get-job-seekers")
    def jobSeekers(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    