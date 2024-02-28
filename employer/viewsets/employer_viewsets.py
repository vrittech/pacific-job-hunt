from ..models import Employer
from ..serializers.employer_serializers import EmployerReadSerializers,EmployerWriteSerializers
from ..utilities.importbase import *

class EmployerViewSets(viewsets.ModelViewSet):
    serializer_class = EmployerReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Employer.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return EmployerWriteSerializers
        return super().get_serializer_class()
    