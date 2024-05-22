from ..models import Education
from ..serializers.education_serializers import EducationListSerializers,EducationRetrieveSerializers,EducationWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class EducationViewset(viewsets.ModelViewSet):
    serializer_class = EducationListSerializers
    permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Education.objects.all()

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
            return EducationWriteSerializers
        elif self.action in ['retrieve']:
            return EducationRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="Educations", url_path="job-seekers")
    # def Educations(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    