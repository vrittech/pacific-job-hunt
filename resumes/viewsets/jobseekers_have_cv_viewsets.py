from ..models import Resumes
from ..serializers.resumes_serializers import ResumesListSerializers,ResumesRetrieveSerializers,ResumesWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class ResumesViewset(viewsets.ModelViewSet):
    serializer_class = ResumesListSerializers
    permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Resumes.objects.all()

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
            return ResumesWriteSerializers
        elif self.action in ['retrieve']:
            return ResumesRetrieveSerializers
        return super().get_serializer_class()
    