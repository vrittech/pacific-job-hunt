from ..models import Skills
from ..serializers.skills_serializers import SkillsReadSerializers,SkillsWriteSerializers
from ..utilities.importbase import *

class SkillsViewSets(viewsets.ModelViewSet):
    serializer_class = SkillsReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Skills.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return SkillsWriteSerializers
        return super().get_serializer_class()
    