from rest_framework import serializers
from ..models import JobLevel

class JobLevelListSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = '__all__'

class JobLevelRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = '__all__'

class JobLevelWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = '__all__'