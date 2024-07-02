from rest_framework import serializers
from ..models import JobsBookmark
from accounts.models import CustomUser
from job.models import Jobs
from jobseeker.models import ProfessionalInformation,JobSeekerHaveSkills

# class JobSeekersHaveSkill_PublicSerializers(serializers.ModelSerializer):
#     name = serializers.SerializerMethodField()
#     experience = serializers.SerializerMethodField()

#     class Meta:
#         model = JobSeekerHaveSkills
#         fields = ['name','experience']
    
#     def get_name(self,obj):
#         return obj.skill.name
    
#     def get_experience(self,obj):
#         return "2"

# class JobSeekersDetail_PublicSerializers(serializers.ModelSerializer):
#     jobseeker_skills = JobSeekersHaveSkill_PublicSerializers(many = True)
#     class Meta:
#         model = ProfessionalInformation
#         fields = '__all__'

# class JobSeekers_PublicSerializers(serializers.ModelSerializer):
#     jobseeker = JobSeekersDetail_PublicSerializers()
#     class Meta:
#         model = CustomUser
#         fields = ['id','first_name','email','last_name','jobseeker']

class Job_PublicSerializers(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
   
    def get_level(self,obj):
        try:
            return obj.level.name
        except:
            return ''
    
    def get_timing(self,obj):
        try:
            return obj.timing.name
        except:
            return ''

    def get_location(self,obj):
        try:
            return obj.location.name
        except:
            return ''
    
    class Meta:
        model = Jobs
        fields = ['id','title','position','level']
        ref_name = "Job_PublicSerializers_JobsBookmark"

class JobsBookmarkPublicListSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = '__all__'

class JobsBookmarkPublicRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = '__all__'

class JobsBookmarkAdminListSerializers(serializers.ModelSerializer):
    job = Job_PublicSerializers()
    class Meta:
        model = JobsBookmark
        fields = '__all__'

class getJobSeekers_JobsBookmarkAdminListReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = ['user','created_date','id','job']
    

class JobsBookmarkAdminRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = '__all__'

class JobsBookmarkWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = '__all__'