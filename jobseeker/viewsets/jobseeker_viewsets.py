from ..models import ProfessionalInformation
from ..serializers.jobseeker_serializers import JobSeekerListSerializers,JobSeekerRetrieveSerializers,JobSeekerWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class ProfessionalInformationViewset(viewsets.ModelViewSet):
    serializer_class = JobSeekerListSerializers
    permission_classes = [JobseekerPermission,IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = ProfessionalInformation.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    filterset_fields = {
        'user':['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)
    
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobSeekerWriteSerializers
        elif self.action in ['list']:
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                return JobSeekerListSerializers
            else:
                return JobSeekerListSerializers
        elif self.action in ['retrieve']:
            
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                print(self.action)
                return JobSeekerRetrieveSerializers
            
            else:
                print(self.action," public retrieve",self.request.user.is_authenticated)
                return JobSeekerRetrieveSerializers
            
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="jobSeekers", url_path="job-seekers")
    # def jobSeekers(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    