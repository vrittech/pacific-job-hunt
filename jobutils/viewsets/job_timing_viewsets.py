from ..models import JobTiming
from ..serializers.job_timing_serializers import JobTimingListSerializers,JobTimingRetrieveSerializers,JobTimingWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class JobTimingViewset(viewsets.ModelViewSet):
    serializer_class = JobTimingListSerializers
    permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobTiming.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'user':['exact'],
    # }
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobTimingWriteSerializers
        elif self.action in ['retrieve']:
            return JobTimingRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="JobTimings", url_path="job-seekers")
    # def JobTimings(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    