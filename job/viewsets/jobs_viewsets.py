from ..models import Jobs
from ..serializers.jobs_serializers import JobReadSerializers,JobWriteSerializers
from ..utilities.importbase import *
from ..utilities.permission import JobPermission

class JobViewSets(viewsets.ModelViewSet):
    serializer_class = JobReadSerializers
    permission_classes = [JobPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Jobs.objects.all()

    def get_queryset(self):
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobWriteSerializers
        return super().get_serializer_class()
    