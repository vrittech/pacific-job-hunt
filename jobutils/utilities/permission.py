from rest_framework.permissions import BasePermission
from accounts import roles

def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN])

def AdminEntrepreneurLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR])

def isOwner(request):
    if str(request.user.id) == str(request.data.get('user')):
        return True
    
    elif len(request.data)==0 and len(request.POST)==0:
        return True

    return False

def isOwnerObject(request,object):
    if object.user_id == request.user.id:
        return True

    return False


class AdminViewSetsPermission(BasePermission):
    def has_permission(self, request, view):    
        return AdminLevel(request)
    

class JobUtilsPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list"]:
            return True
        elif view.action in ['retrieve']:
            return True
        elif view.action in ['create','update']:
            return AdminLevel(request)
        elif view.action == "partial_update":
            return AdminLevel(request)
        elif view.action == 'destroy':
            return AdminLevel(request)
