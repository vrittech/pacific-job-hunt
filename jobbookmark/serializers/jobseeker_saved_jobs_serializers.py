from rest_framework import serializers
from ..models import JobsBookmark
from job.models import Jobs

class Job_PublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['id','title','position','level']
        ref_name = "Job_PublicSerializers_JobsBookmark"

class JobsBookmarkPublicListSerializers(serializers.ModelSerializer):
    is_apply = serializers.SerializerMethodField()

    class Meta:
        model = JobsBookmark
        fields = '__all__'
    
    def get_is_apply(self,obj):
        user = self.context.get('user')
        if user.is_authenticated:
            return user.apply_jobs.all().filter(job_id = obj.id).exists()
        return False

class JobsBookmarkPublicRetrieveSerializers(serializers.ModelSerializer):
    is_apply = serializers.SerializerMethodField()
    
    class Meta:
        model = JobsBookmark
        fields = '__all__'

    def get_is_apply(self,obj):
        user = self.context.get('user')
        if user.is_authenticated:
            return user.apply_jobs.all().filter(job_id = obj.id).exists()
        return False

class getJobSeekers_JobsBookmarkAdminListReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = ['user','created_date','id','job']


class JobsBookmarkWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsBookmark
        fields = '__all__'