from ..models import JobSeeker
from ..serializers.jobseeker_serializers import JobSeekerReadSerializers,JobSeekerWriteSerializers
from ..utilities.importbase import *

class JobSeekerViewSets(viewsets.ModelViewSet):
    serializer_class = JobSeekerReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobSeeker.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobSeekerWriteSerializers
        return super().get_serializer_class()
    