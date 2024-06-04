from rest_framework import serializers
from ..models import Company,CompanyType
import ast

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
        if data.get('interest'):
            data = str_to_list(data,'type')
            return super().to_internal_value(data)
        return super().to_internal_value(data)
    
    class Meta:
        model = Company
        fields = '__all__'