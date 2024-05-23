from ..models import JobSeekerHaveSkills
from ..serializers.jobseeker_have_skills_serializers import JobSeekerHaveSkillsListSerializers,JobSeekerHaveSkillsRetrieveSerializers,JobSeekerHaveSkillsWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class JobSeekerHaveSkillsViewset(viewsets.ModelViewSet):
    serializer_class = JobSeekerHaveSkillsListSerializers
    permission_classes = [JobseekerPermission,IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobSeekerHaveSkills.objects.all()

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
            return JobSeekerHaveSkillsWriteSerializers
        elif self.action in ['list']:
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                return JobSeekerHaveSkillsListSerializers
            else:
                return JobSeekerHaveSkillsListSerializers
        elif self.action in ['retrieve']:
            
            if self.request.user.is_authenticated and self.request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR]:
                print(self.action)
                return JobSeekerHaveSkillsRetrieveSerializers
            
            else:
                print(self.action," public retrieve",self.request.user.is_authenticated)
                return JobSeekerHaveSkillsRetrieveSerializers
            
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="JobSeekerHaveSkillss", url_path="job-seekers")
    # def JobSeekerHaveSkillss(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    