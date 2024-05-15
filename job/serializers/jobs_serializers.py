from rest_framework import serializers
from ..models import Jobs
from company.models import Company

class Company_PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields =  '__all__'

class JobListPublicSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobListAdminSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobRetrieveAdminSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobRetrievePublicSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
