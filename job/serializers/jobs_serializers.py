from rest_framework import serializers
from ..models import Jobs
from company.models import Company
from ..models import JobCategory

class Company_PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields =  ['company_name','company_slug','company_logo','location']

class JobCategory_PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields =  ['name','slug']

class JobListPublicSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobListAdminSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobRetrieveAdminSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobRetrievePublicSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
