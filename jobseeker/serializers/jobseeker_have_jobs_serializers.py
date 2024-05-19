from rest_framework import serializers
from ..models import JobsApply
from accounts.models import CustomUser
from job.models import Jobs

class JobSeekers_PublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','email','last_name']

class Job_PublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['id','title','position','level']

class JobsApplyPublicListSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsApply
        fields = '__all__'

class JobsApplyPublicRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsApply
        fields = '__all__'

class JobsApplyAdminListSerializers(serializers.ModelSerializer):
    user = JobSeekers_PublicSerializers()
    job = Job_PublicSerializers()
    class Meta:
        model = JobsApply
        fields = '__all__'

class getJobSeekers_JobsApplyAdminListReadSerializers(serializers.ModelSerializer):
    user = JobSeekers_PublicSerializers()
    class Meta:
        model = JobsApply
        fields = ['user']

class JobsApplyAdminRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsApply
        fields = '__all__'

class JobsApplyWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobsApply
        fields = '__all__'