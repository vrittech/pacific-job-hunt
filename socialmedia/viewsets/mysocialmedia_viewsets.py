from ..models import MySocialMedia
from ..serializers.my_social_media_serializers import MySocialMediaListSerializers,MySocialMediaRetrieveSerializers,MySocialMediaWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class MySocialMediaViewset(viewsets.ModelViewSet):
    serializer_class = MySocialMediaListSerializers
    # permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = MySocialMedia.objects.all()

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
            return MySocialMediaWriteSerializers
        elif self.action in ['retrieve']:
            return MySocialMediaRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="MySocialMedias", url_path="job-seekers")
    # def MySocialMedias(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    