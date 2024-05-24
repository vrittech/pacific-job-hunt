from rest_framework.permissions import BasePermission
from accounts import roles

def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN])

def AdminEntrepreneurLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [roles.ADMIN,roles.SUPER_ADMIN,roles.ENTREPRENEUR])

def CompanyOwnerJob(request,object):
    print(str(object.job.company.owner_id) == str(request.user.id),str(object.job.company.owner_id), str(request.user.id))
    
    if str(object.job.company.owner_id) == str(request.user.id):
        return True
    else:
        pass


def isOwner(request):
    if str(request.user.id) == str(request.data.get('user')):
        return True
    
    elif len(request.data)==0 and len(request.POST)==0:
        return True

    return False

def isOwnerObject(request,object):
    if str(object.user_id) == str(request.user.id):
        return True
    return False

class AdminViewSetsPermission(BasePermission):
    def has_permission(self, request, view):    
        return AdminLevel(request)
    
class JobSeekersApplySavedJobPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action in ['jobSeekers']:
            return True
        elif view.action in ['retrieve']    :
            # return True
            return isOwnerObject(request,view.get_object()) or CompanyOwnerJob(request,view.get_object())
        elif view.action in ['create']:
            return isOwner(request)
        elif view.action in ['destroy']:
            return CompanyOwnerJob(request,view.get_object())
        elif view.action in ['partial_update']:
            return CompanyOwnerJob(request,view.get_object())
        else:
            return False

class JobseekerPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list"]:
            return True
        elif view.action in ['retrieve']:
            return isOwnerObject(request,view.get_object())
        elif view.action in ['create','update']:
            return isOwner(request)
        elif view.action == "partial_update":
            return view.get_object().user_id == request.user.id
        elif view.action == 'destroy':
            return isOwnerObject(request,view.get_object())
            
        else:
            return False

