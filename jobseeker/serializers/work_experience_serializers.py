from rest_framework import serializers
from ..models import WorkExperience

class WorkExperienceListPublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class WorkExperienceRetrievePublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class WorkExperienceListAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class WorkExperienceRetrieveAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class WorkExperienceWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'