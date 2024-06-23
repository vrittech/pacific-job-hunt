from ..models import JobLocation
from ..serializers.job_location_serializers import JobLocationListSerializers,JobLocationRetrieveSerializers,JobLocationWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class JobLocationViewset(viewsets.ModelViewSet):
    serializer_class = JobLocationListSerializers
    permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobLocation.objects.all()

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
            return JobLocationWriteSerializers
        elif self.action in ['retrieve']:
            return JobLocationRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="JobLocations", url_path="job-seekers")
    # def JobLocations(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    