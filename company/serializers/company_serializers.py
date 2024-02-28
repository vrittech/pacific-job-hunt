from rest_framework import serializers
from ..models import Company

class CompanyReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'