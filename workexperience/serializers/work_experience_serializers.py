from rest_framework import serializers
from ..models import WorkExperience

class WorkExperienceListSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class WorkExperienceRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class WorkExperienceWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'