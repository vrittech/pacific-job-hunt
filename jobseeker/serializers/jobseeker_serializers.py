from rest_framework import serializers
from ..models import JobSeeker

class JobSeekerListPublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class JobSeekerRetrievePublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class JobSeekerListAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class JobSeekerRetrieveAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class JobSeekerWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'