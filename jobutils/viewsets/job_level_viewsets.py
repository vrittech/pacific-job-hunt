from ..models import JobLevel
from ..serializers.job_level_serializers import JobLevelListSerializers,JobLevelRetrieveSerializers,JobLevelWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class JobLevelViewset(viewsets.ModelViewSet):
    serializer_class = JobLevelListSerializers
    permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobLevel.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'user':['exact'],
    # }
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)
    
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobLevelWriteSerializers
        elif self.action in ['retrieve']:
            return JobLevelRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="JobLevels", url_path="job-seekers")
    # def JobLevels(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    