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


class JobCategory_JobRetrieveAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields =  ['name','slug','id']        

class JobListPublicSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    is_apply = serializers.SerializerMethodField()
    is_save = serializers.SerializerMethodField()
    class Meta:
        model = Jobs
        fields = '__all__'
    
    def get_is_apply(self,obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.apply_jobs.all().filter(job_id = obj.id).exists()
        return False
    
    def get_is_save(self,obj):
        # return False
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.saved_jobs.all().filter(job_id = obj.id).exists()
        return False
    
class JobListAdminSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobRetrieveAdminSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_JobRetrieveAdminSerializer(read_only = True)
    class Meta:
        model = Jobs
        fields = '__all__'

class JobRetrievePublicSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    is_apply = serializers.SerializerMethodField()
    is_save = serializers.SerializerMethodField()
    class Meta:
        model = Jobs
        fields = '__all__'

    def get_is_apply(self,obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.apply_jobs.all().filter(job_id = obj.id).exists()
        return False
    
    def get_is_save(self,obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.saved_jobs.all().filter(job_id = obj.id).exists()
        return False

class JobWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
