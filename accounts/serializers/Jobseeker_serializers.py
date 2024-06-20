from rest_framework import serializers
from ..models import CustomUser
from jobseeker.models import ProfessionalInformation,Profession
from socialmedia.models import SocialMedia,MySocialMedia
from education.models import Education
from workexperience.models import WorkExperience
from jobapply.models import JobsApply


class EducationSerializers(serializers.ModelSerializer):
      class Meta:
        ref_name = "EducationJobseekers"
        model = Education
        fields = '__all__'

class WorkExperienceSerializers(serializers.ModelSerializer):
      class Meta:
        ref_name = "WorkExperienceJobseekers"
        model = WorkExperience
        fields = '__all__'

class SocialMediaSerializers(serializers.ModelSerializer):
      class Meta:
        ref_name = "SocialMediaSerializers"
        model = SocialMedia
        fields = ['name','image'] 

class MySocialMediaSerializers(serializers.ModelSerializer):
      social_media = SocialMediaSerializers()
      class Meta:
        ref_name = "SocialMediaSerializers"
        model = MySocialMedia
        fields = ['url','social_media']

class ProfessionSerializers(serializers.ModelSerializer):
      class Meta:
        ref_name = "ProfessionSerializers"
        model = Profession
        fields = ['name'] 

class ProfessionalInformationSerializers(serializers.ModelSerializer):
      profession = ProfessionSerializers()
      class Meta:
        model = ProfessionalInformation
        fields = ['experience','profession','cv'] 


class JobseekersDetailSerializers(serializers.ModelSerializer):
    professional_information  = ProfessionalInformationSerializers()
    applied_jobs = serializers.SerializerMethodField()
    social_media = MySocialMediaSerializers(many = True)
    educations = EducationSerializers(many = True)
    work_experience = WorkExperienceSerializers(many = True)
    job_detail = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','username','created_date','applied_jobs','professional_information','social_media','educations','work_experience','job_detail'] 

    def get_applied_jobs(self,obj):
        return 12
    
    def get_job_detail(self,obj):
        return "Job"
        
        
    

