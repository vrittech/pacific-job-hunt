from rest_framework.permissions import BasePermission
from accounts import roles

def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN])

def AdminEntrepreneurLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR])

def isOwner(request):
    if str(request.user.id) == str(request.data.get('owner')):
        return True
    return False

def isOwnerCompany(request,object):
    if object.owner_id == request.user.id:
        return True
    return False

class AdminViewSetsPermission(BasePermission):
    def has_permission(self, request, view): 
        if view.action in ["list","retrieve"]:
            return True
        return AdminLevel(request)
    
class CompanyPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list","retrieve"]:
            return True
        elif view.action in ['create','update']:
            return AdminLevel(request) or (AdminEntrepreneurLevel(request) and isOwner(request))
        elif view.action in ['signUpCompany']:
            return True
        elif view.action == "partial_update":
            return view.get_object().owner_id == request.user.id or AdminLevel(request)
        elif view.action == 'destroy':
            return AdminLevel(request) or (AdminEntrepreneurLevel(request) and isOwnerCompany(request,view.get_object()))
        