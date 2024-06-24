from rest_framework import serializers
from ..models import JobsBookmark
from job.models import Jobs
from company.models import Company
from professions.models import Profession

class Profession_PublicSerializerJobSaved(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields =  ['name','id']

class Company_PublicSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "jobsaved"
        model = Company
        fields = ['company_name','company_slug','type','company_logo','company_banner','location']

class Job_PublicSerializers(serializers.ModelSerializer):
    company = Company_PublicSerializers()
    position = Profession_PublicSerializerJobSaved()
    level = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    timing = serializers.SerializerMethodField()

    def get_level(self,obj):
        return obj.level.name
    
    def get_level(self,obj):
        return obj.location.name

    def get_level(self,obj):
        return obj.timing.name
    
    class Meta:
        model = Jobs
        fields = ['id','title','position','level','location','required_number','company','image','created_date','salary_mode','min_salary','max_salary','timing','expiry_date']
        ref_name = "Job_PublicSerializers_JobsBookmark"

class JobsBookmarkPublicListSerializers(serializers.ModelSerializer):
    is_apply = serializers.SerializerMethodField()
    job = Job_PublicSerializers()
    class Meta:
        model = JobsBookmark
        fields = '__all__'
    
    def get_is_apply(self,obj):
        user = self.context.get('request').user
        print(user.is_authenticated, " user logined" )
        if user.is_authenticated:
            return user.apply_jobs.all().filter(job_id = obj.job_id).exists()
        return False

class JobsBookmarkPublicRetrieveSerializers(serializers.ModelSerializer):
    is_apply = serializers.SerializerMethodField()
    
    class Meta:
        model = JobsBookmark
        fields = '__all__'

    def get_is_apply(self,obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.apply_jobs.all().filter(job_id = obj.job_id).exists()
        return False

class getJobSeekers_JobsBookmarkAdminListReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = ['user','created_date','id','job']


class JobsBookmarkWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = '__all__'