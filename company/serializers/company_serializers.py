from rest_framework import serializers
from ..models import Company,CompanyType
import ast
from accounts.models import CustomUser

def str_to_list(data,value_to_convert):
    mutable_data = data.dict()
    value_to_convert_data = mutable_data[value_to_convert]
    if type(value_to_convert_data) == list:
        return mutable_data
    try:
        variations = ast.literal_eval(value_to_convert_data)
        mutable_data[value_to_convert] = variations
        return mutable_data
    except ValueError as e:
        raise serializers.ValidationError({f'{value_to_convert}': str(e)})

class CompanyTypePublicSerializers_CompanyReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'

class CompanyReadSerializers(serializers.ModelSerializer):
    type = CompanyTypePublicSerializers_CompanyReadSerializers(many = True)
    class Meta:
        model = Company
        fields = ['id','company_name','company_slug','type','mobile_number','email','company_logo','company_banner','about','company_size','website','is_verified','owner','location','created_date','total_active_job']

class CompanySerializers(serializers.ModelSerializer):

    def to_internal_value(self, data):
        if data.get('type'):
            if isinstance(data.get('type'), str):
                data = str_to_list(data,'type')
                return super().to_internal_value(data)
        return super().to_internal_value(data)
    
    class Meta:
        model = Company
        fields = '__all__'

    def get_fields(self):
        fields = super(CompanySerializers, self).get_fields()
        # Check if the request method is PUT or PATCH
        request = self.context.get('request')
        if request and request.method in ['PUT', 'PATCH']:
            fields['owner'].read_only = True

        return fields


class signUpCompanySerializers(serializers.ModelSerializer):
    
    password = serializers.CharField()
    owner_email = serializers.EmailField()
    email = serializers.EmailField()
    mobile_number = serializers.CharField()
    owner_name = serializers.CharField()
    company_name = serializers.CharField()
    company_slug = serializers.CharField()
    class Meta:
        model = Company
        fields = ['password','owner_email','email','mobile_number','owner_name','type','company_slug','company_name']
    
class CustomUserSerializer_CompanySignup(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
