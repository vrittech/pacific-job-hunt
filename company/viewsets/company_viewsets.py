from ..models import Company
from ..serializers.company_serializers import CompanyReadSerializers,CompanySerializers
from ..utilities.importbase import *
from ..utilities.permission import CompanyPermission
from django.db.models import Count, Q
from django.utils import timezone

class CompanyViewSets(viewsets.ModelViewSet):
    serializer_class = CompanyReadSerializers
    permission_classes = [CompanyPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = Company.objects.annotate(total_active_jobs=Count('jobs', filter=Q(jobs__is_active=True, jobs__is_verified=True, jobs__expiry_date__gte=timezone.now())))
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['company_name','company_slug','website','location']
    ordering_fields = ['id','company_slug','total_active_jobs']
    filterset_fields = {
        'company_slug': ['exact', 'icontains'],
        'type':['exact'],
        'owner': ['exact'],
        'location':['icontains'],
    }

    lookup_field = "company_slug"
    def get_serializer_class(self):
        print(self.queryset)
        if self.action in ['create','update','partial_update']:
            return CompanySerializers
        return super().get_serializer_class()
    