from ..models import WorkExperience
from ..serializers.work_experience_serializers import WorkExperienceListSerializers,WorkExperienceRetrieveSerializers,WorkExperienceWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class WorkExprienceViewset(viewsets.ModelViewSet):
    serializer_class = WorkExperienceListSerializers
    permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = WorkExperience.objects.all()

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
            return WorkExperienceWriteSerializers
        elif self.action in ['retrieve']:
            return WorkExperienceRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="WorkExperiences", url_path="job-seekers")
    # def WorkExperiences(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    