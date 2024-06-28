from ..models import Company
from ..serializers.company_serializers import CompanyReadSerializers,CompanySerializers,signUpCompanySerializers,CustomUserSerializer_CompanySignup
from ..utilities.importbase import *
from ..utilities.permission import CompanyPermission
from django.db.models import Count, Q
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from accounts.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.db import transaction
from accounts import roles
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken,TokenError


class CompanyViewSets(viewsets.ModelViewSet):
    serializer_class = CompanyReadSerializers
    permission_classes = [CompanyPermission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = Company.objects.annotate(total_active_jobs=Count('jobs', filter=Q(jobs__is_active=True, jobs__is_verified=True, jobs__expiry_date__gte=timezone.now())))
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['company_name','company_slug','website','location']
    ordering_fields = ['id','company_slug','total_active_jobs']
    filterset_fields = {
        'company_slug': ['exact', 'icontains'],
        'type':['exact'],
        'owner': ['exact'],
        'location':['icontains'],
    }

    lookup_field = "company_slug"
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CompanySerializers
        elif self.action in ['signUpCompany']:
            return signUpCompanySerializers
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @transaction.atomic
    @action(detail=False, methods=['post'], name="signUpCompany", url_path="signup-company")
    def signUpCompany(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Company.objects.filter(company_slug = serializer.validated_data.get('company_slug')).exists():
            return Response({'message':'This company already exists'},status=status.HTTP_400_BAD_REQUEST)
    
        user_data = {
            'email': serializer.validated_data.get('owner_email'),
            'username':serializer.validated_data.get('owner_email').split('@')[0],
            'role': roles.ENTREPRENEUR,
            'password':make_password(serializer.validated_data.get('password')),
        }
        create_user = createUser(user_data)
        try:
            user_obj = CustomUser.objects.filter(id = create_user.get('id'))
            refresh = RefreshToken.for_user(user_obj.first())
            access = str(refresh.access_token)
            refresh = str(refresh)

            user_data['access'] = access
            user_data['is_verified'] = user_obj.first().is_verified
            user_data['refresh'] = refresh
        except:
            pass

        company_data = {
            'company_name': serializer.validated_data.get('company_name'),
            'type': [company_type.id for company_type in serializer.validated_data.get('type')],
            'company_slug':serializer.validated_data.get('company_slug'),
            'mobile_number': serializer.validated_data.get('mobile_number'),
            'email': serializer.validated_data.get('email'),
            'owner':create_user.get('id'),
        }

        company_obj = createCompany(company_data)
        return Response({"message": "created successfully","user_data":user_data,"company_data":company_obj})


def createUser(data):
    user_serializers = CustomUserSerializer_CompanySignup(data=data)
    user_serializers.is_valid(raise_exception=True)
    user_serializers.save()
    return user_serializers.data

def createCompany(data):
    company_serializers = CompanySerializers(data=data)
    company_serializers.is_valid(raise_exception=True)
    company_serializers.save()
    return company_serializers.data
    
    
    