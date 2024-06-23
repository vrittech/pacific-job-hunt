from ..models import JobPosition
from ..serializers.job_position_serializers import JobPositionListSerializers,JobPositionRetrieveSerializers,JobPositionWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class JobPositionViewset(viewsets.ModelViewSet):
    serializer_class = JobPositionListSerializers
    permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobPosition.objects.all()

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
            return JobPositionWriteSerializers
        elif self.action in ['retrieve']:
            return JobPositionRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="JobPositions", url_path="job-seekers")
    # def JobPositions(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    