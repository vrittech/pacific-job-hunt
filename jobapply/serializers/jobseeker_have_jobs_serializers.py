from rest_framework import serializers
from ..models import JobsApply
from accounts.models import CustomUser
from job.models import Jobs
from jobseeker.models import ProfessionalInformation,JobSeekerHaveSkills
from company.models import Company
from professions.models import Profession
from resumes.models import Resumes


class Resumes_getJobSeekers_JobsApplyAdminListReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields =  ['cv']

class Profession_JobApplyPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields =  ['name','id']

class JobSeekersHaveSkill_PublicSerializers(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()

    class Meta:
        model = JobSeekerHaveSkills
        fields = ['name','experience']
    
    def get_name(self,obj):
        return obj.skill.name
    
    def get_experience(self,obj):
        return "2"

class Professional_information_PublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'

class JobSeekers_PublicSerializers(serializers.ModelSerializer):
    professional_information = Professional_information_PublicSerializers()
    jobseeker_skills = JobSeekersHaveSkill_PublicSerializers(many = True)
    class Meta:
        model = CustomUser
        fields = ['id','first_name','email','last_name','professional_information','jobseeker_skills']

class Company_PublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name','company_slug','type','company_logo','company_banner','location']

class Job_PublicSerializers(serializers.ModelSerializer):
    company = Company_PublicSerializers()
    position = Profession_JobApplyPublicSerializer()
    level = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    timing = serializers.SerializerMethodField()

    def get_level(self,obj):
        return obj.level.name
    
    def get_location(self,obj):
        return obj.location.name

    def get_timing(self,obj):
        return obj.timing.name
    
    class Meta:
        model = Jobs
        fields = ['id','title','position','level','location','required_number','company','image','created_date','salary_mode','min_salary','max_salary','timing','expiry_date']

class JobsApplyPublicListSerializers(serializers.ModelSerializer):
    job = Job_PublicSerializers()
    class Meta:
        model = JobsApply
        fields = '__all__'

class JobsApplyPublicRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsApply
        fields = '__all__'

class JobsApplyAdminListSerializers(serializers.ModelSerializer):
    user = JobSeekers_PublicSerializers()
    # job = Job_PublicSerializers()
    class Meta:
        model = JobsApply
        fields = '__all__'

class getJobSeekers_JobsApplyAdminListReadSerializers(serializers.ModelSerializer):
    user = JobSeekers_PublicSerializers()
    cv = Resumes_getJobSeekers_JobsApplyAdminListReadSerializers()
    class Meta:
        model = JobsApply
        fields = ['user','created_date','status','id','job','is_saved_applicant','cv']
    

class JobsApplyAdminRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsApply
        fields = '__all__'

class JobsApplyWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsApply
        fields = '__all__'