from ..models import Company
from ..serializers.company_serializers import CompanyReadSerializers,CompanySerializers
from ..utilities.importbase import *
from ..utilities.permission import CompanyPermission

class CompanyViewSets(viewsets.ModelViewSet):
    serializer_class = CompanyReadSerializers
    permission_classes = [CompanyPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Company.objects.all()

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['company_name','company_slug','website','location']
    ordering_fields = ['id','company_slug']
    filterset_fields = {
        'company_slug': ['exact', 'icontains'],
        'type':['exact'],
        'owner': ['exact'],
    }

    lookup_field = "company_slug"
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CompanySerializers
        return super().get_serializer_class()
    