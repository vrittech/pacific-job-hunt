from ..models import JobCategory
from ..serializers.job_category_serializers import JobCategoryReadSerializers,JobCategoryWriteSerializers
from ..utilities.importbase import *
from ..utilities.permission import JobCategoryPermission

class JobsCategoryViewSets(viewsets.ModelViewSet):
    serializer_class = JobCategoryReadSerializers
    permission_classes = [JobCategoryPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = JobCategory.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return JobCategoryWriteSerializers
        return super().get_serializer_class()
    