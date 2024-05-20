from ..models import ProfessionalInformation
from ..serializers.jobseeker_serializers import JobSeekerListPublicSerializers,JobSeekerRetrievePublicSerializers,JobSeekerListAdminSerializers,JobSeekerRetrieveAdminSerializers,JobSeekerWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class ProfessionalInformationViewset(viewsets.ModelViewSet):
    serializer_class = JobSeekerRetrieveAdminSerializers
    permission_classes = [AdminViewSetsPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = ProfessionalInformation.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    filterset_fields = {
        'user':['exact'],
    }

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobSeekerWriteSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="jobSeekers", url_path="job-seekers")
    # def jobSeekers(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    