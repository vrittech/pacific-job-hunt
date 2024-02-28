from rest_framework import serializers
from ..models import CompanyType

class CompanyTypeReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'

class CompanyTypeWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'