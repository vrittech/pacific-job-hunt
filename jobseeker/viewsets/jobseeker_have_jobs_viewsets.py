from ..models import JobsApply
from ..serializers.jobseeker_have_jobs_serializers import JobsApplyReadSerializers,JobsApplyWriteSerializers
from ..utilities.importbase import *

class EmployerHaveJobsViewSets(viewsets.ModelViewSet):
    serializer_class = JobsApplyReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobsApply.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobsApplyWriteSerializers
        return super().get_serializer_class()
    