from ..models import JobsApply
from ..serializers.jobseeker_have_jobs_serializers import (
    JobsApplyPublicListSerializers,JobsApplyPublicRetrieveSerializers,
    JobsApplyAdminListSerializers,JobsApplyAdminRetrieveSerializers,
    getJobSeekers_JobsApplyAdminListReadSerializers,
    JobsApplyWriteSerializers
    )

from rest_framework.response import Response

from ..utilities.importbase import *
from accounts import roles
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class JobSeekerHaveJobsViewSets(viewsets.ModelViewSet):
    serializer_class = JobsApplyPublicListSerializers
    permission_classes = [IsAuthenticated,JobSeekersApplySavedJobPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobsApply.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['user__email','user__username']
    ordering_fields = ['id']

    filterset_fields = {
        'user':['exact'],
        'job':['exact'],
        'status':['exact'],
        'is_saved_applicant':['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.role == roles.JOBSEEKER:
            return queryset.filter(user = user)
        elif user.role in [roles.ENTREPRENEUR]:
            return queryset.filter(job__company__owner = user)
        elif user in [roles.ADMIN]:
            return queryset
        else:
            return queryset.none()

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
    def jobSeekers(self, request, *args, **kwargs):#this response some additional data for admin,admin try to get some detail
        return super().list(request, *args, **kwargs)
    

    @action(detail=False, methods=['post'], name="JobSeekersBulkStatus", url_path="job-seekers-bulk-status")
    def JobSeekersBulkStatus(self, request, *args, **kwargs):#this response some additional data for admin,admin try to get some detail
        job_applys_id = request.data.get('job_applys_id')
        status = request.data.get('status')
      
        if job_applys_id:
            applier_objs = JobsApply.objects.filter(id__in = job_applys_id,job__company__owner = request.user.id)
            deleted_count, _ = applier_objs.update(status = status)
           
            return Response({'message': f'Successfully  {status} jobseekers'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':f'can not {status} jobseekers'},status=status.HTTP_400_BAD_REQUEST)

    
    
    