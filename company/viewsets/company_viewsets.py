from ..models import Company
from ..serializers.company_serializers import CompanyReadSerializers,CompanySerializers
from ..utilities.importbase import *

class CompanyViewSets(viewsets.ModelViewSet):
    serializer_class = CompanyReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Company.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CompanySerializers
        return super().get_serializer_class()
    