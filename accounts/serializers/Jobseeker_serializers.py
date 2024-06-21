from rest_framework import serializers
from ..models import CustomUser
from jobseeker.models import ProfessionalInformation,Profession,JobSeekerHaveSkills
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
        fields = ['experience','profession','cv','about'] 

class JobSeekerHaveSkillsSerializers_JobseekersDetailSerializers(serializers.ModelSerializer):
      skill = serializers.SerializerMethodField()
      class Meta:
        model = JobSeekerHaveSkills
        fields = ['skill','experience']

      def get_skill(self,obj):
          return obj.skill.name

class JobsApplySerializers__JobseekersDetailSerializers(serializers.ModelSerializer):
      cv = serializers.SerializerMethodField()
      class Meta:
        model = JobsApply
        fields = ['status','cv','is_saved_applicant','cover_letter_file','cover_letter_str','location','phone_number']
      
      def get_cv(self,obj):
            request = self.context.get('request')
            if obj.cv:
              cv_url = obj.cv.cv.url
              full_cv_url = request.build_absolute_uri(cv_url)
              return full_cv_url


class JobseekersDetailSerializers(serializers.ModelSerializer):
    professional_information  = ProfessionalInformationSerializers()
    applied_jobs = serializers.SerializerMethodField()
    social_media = MySocialMediaSerializers(many = True)
    educations = EducationSerializers(many = True)
    jobseeker_skills = JobSeekerHaveSkillsSerializers_JobseekersDetailSerializers(many = True)
    work_experience = WorkExperienceSerializers(many = True)
    job_detail = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['image','id','email','first_name','last_name','username','created_date','applied_jobs','professional_information','social_media','educations','work_experience','job_detail','jobseeker_skills','gender'] 

    def get_applied_jobs(self,obj):
        return 12
    
    def get_job_detail(self,obj):
        request = self.context['request']
        kwargs = {
            'request':request,
        }
        job_applied_id = request.GET.get('applied_id')
        if job_applied_id:
            jobapply_obj =JobsApply.objects.filter(id = job_applied_id)
            if jobapply_obj.exists():
                job_applied_detail = JobsApplySerializers__JobseekersDetailSerializers(jobapply_obj.first(),many = False,context={'request': request})
                return job_applied_detail.data
        
    

