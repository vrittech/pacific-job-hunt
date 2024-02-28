from ..models import Company
from ..serializers.job_category_serializers import JobCategoryReadSerializers,JobCategoryWriteSerializers
from ..utilities.importbase import *

class JobsCategoryViewSets(viewsets.ModelViewSet):
    serializer_class = JobCategoryReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Company.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobCategoryWriteSerializers
        return super().get_serializer_class()
    