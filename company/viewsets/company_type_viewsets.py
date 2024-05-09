from ..models import CompanyType
from ..serializers.company_type_serializers import CompanyTypeReadSerializers,CompanyTypeWriteSerializers
from ..utilities.importbase import *

class CompanytypeViewSets(viewsets.ModelViewSet):
    serializer_class = CompanyTypeReadSerializers
    permission_classes = [AdminViewSetsPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = CompanyType.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CompanyTypeWriteSerializers
        return super().get_serializer_class()
    