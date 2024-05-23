from ..models import SocialMedia
from ..serializers.social_media_serializers import SocialMediaListSerializers,SocialMediaRetrieveSerializers,SocialMediaWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action

class SocialMediaViewset(viewsets.ModelViewSet):
    serializer_class = SocialMediaListSerializers
    # permission_classes = [JobseekerPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = SocialMedia.objects.all()

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
            return SocialMediaWriteSerializers
        elif self.action in ['retrieve']:
            return SocialMediaRetrieveSerializers
        return super().get_serializer_class()
    
    # @action(detail=False, methods=['get'], name="SocialMedias", url_path="job-seekers")
    # def SocialMedias(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    