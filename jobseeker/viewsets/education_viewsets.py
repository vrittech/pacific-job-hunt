from ..models import Education
from ..serializers.education_serializers import EducationListPublicSerializers,EducationRetrievePublicSerializers,EducationListAdminSerializers,EducationRetrieveAdminSerializers,EducationWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class EducationViewset(viewsets.ModelViewSet):
    serializer_class = EducationRetrieveAdminSerializers
    # permission_classes = [AdminViewSetsPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Education.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'user':['exact'],
    # }

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return EducationWriteSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="Educations", url_path="job-seekers")
    # def Educations(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    