from ..models import Jobs
from ..serializers.jobs_serializers import JobListPublicSerializer,JobListAdminSerializer,JobRetrievePublicSerializer,JobRetrieveAdminSerializer,JobWriteSerializers
from ..utilities.importbase import *
from ..utilities.permission import JobPermission

class JobViewSets(viewsets.ModelViewSet):
    serializer_class = JobListPublicSerializer
    permission_classes = [JobPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Jobs.objects.all()

    def get_queryset(self):
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobWriteSerializers
        elif self.action in ['list']:
            return JobListPublicSerializer
        elif self.action in ['retrieve']:
            return JobRetrievePublicSerializer
        return super().get_serializer_class()
    