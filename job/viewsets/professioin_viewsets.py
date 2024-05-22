from ..models import Profession
from ..serializers.profession_serializers import ProfessionReadSerializers,ProfessionWriteSerializers
from ..utilities.importbase import *
from ..utilities.permission import JobCategoryPermission

class ProfessionViewSets(viewsets.ModelViewSet):
    serializer_class = ProfessionReadSerializers
    permission_classes = [JobCategoryPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Profession.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return ProfessionWriteSerializers
        return super().get_serializer_class()
    