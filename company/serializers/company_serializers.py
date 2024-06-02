from rest_framework import serializers
from ..models import Company,CompanyType

class CompanyTypePublicSerializers_CompanyReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'

class CompanyReadSerializers(serializers.ModelSerializer):
    type = CompanyTypePublicSerializers_CompanyReadSerializers(many = True)
    class Meta:
        model = Company
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'