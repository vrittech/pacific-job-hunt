from ..models import JobsBookmark
from ..serializers.jobseeker_saved_jobs_serializers import (
    JobsBookmarkPublicListSerializers,JobsBookmarkPublicRetrieveSerializers,
    JobsBookmarkAdminListSerializers,JobsBookmarkAdminRetrieveSerializers,
    getJobSeekers_JobsBookmarkAdminListReadSerializers,
    JobsBookmarkWriteSerializers
    )

from ..utilities.importbase import *
from accounts import roles
from rest_framework.decorators import action

class JobSeekerHaveSavedJobsViewSets(viewsets.ModelViewSet):
    serializer_class = JobsBookmarkPublicListSerializers
    permission_classes = [JobSeekersApplySavedJobPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobsBookmark.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    filterset_fields = {
        'user':['exact'],
        'job':['exact'],
        'status':['exact'],

    }

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobsBookmarkWriteSerializers
        elif self.action in ['jobSeekers']:
            return getJobSeekers_JobsBookmarkAdminListReadSerializers
        elif self.action in ['list']:
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                return JobsBookmarkAdminListSerializers
            else:
                return JobsBookmarkPublicListSerializers
        elif self.action in ['retrieve']:
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                return JobsBookmarkAdminRetrieveSerializers
            else:
                return JobsBookmarkPublicRetrieveSerializers
            
        return super().get_serializer_class()
    
    @action(detail=False, methods=['get'], name="jobSeekers", url_path="get-job-seekers")
    def jobSeekers(self, request, *args, **kwargs): #this response some additional data for admin,admin try to get some detail
        return super().list(request, *args, **kwargs)
    
    
    