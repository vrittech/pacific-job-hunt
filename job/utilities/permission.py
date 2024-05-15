from rest_framework.permissions import BasePermission
from accounts import roles
from company.models import Company

def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN])

def AdminEntrepreneurLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR])

class AdminViewSetsPermission(BasePermission):
    def has_permission(self, request, view):
        return AdminLevel(request)
    
def isCompanyOwner(request):
    company = Company.objects.filter(id = request.data.get('company_id'),owner_id = request.user.id)
    if company.exists():
        return True
    return False

def isOwnerJob(request,object):
    if object.company.owner_id == request.user.id:
        return True
    return False

class JobPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list','retrieve']:
            return True
        elif view.action in ['update','partial_update','create']:
            return AdminEntrepreneurLevel(request) and isCompanyOwner(request)
        elif view.action == "destroy":
            return AdminLevel(request) or (IsAuthenticated(request) and isOwnerJob(request,view.get_object()))
        else:
            return False
        