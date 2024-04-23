from rest_framework import serializers
from ..models import JobSeeker

class JobSeekerReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class JobSeekerWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'