from ..models import EducationLevel
from ..serializers.education_level_serializers import EducationLevelListSerializers,EducationLevelRetrieveSerializers,EducationLevelWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class EducationLevelViewset(viewsets.ModelViewSet):
    serializer_class = EducationLevelListSerializers
    permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = EducationLevel.objects.all()

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
            return EducationLevelWriteSerializers
        elif self.action in ['retrieve']:
            return EducationLevelRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="EducationLevels", url_path="job-seekers")
    # def EducationLevels(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    