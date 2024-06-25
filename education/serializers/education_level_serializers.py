from rest_framework import serializers
from ..models import EducationLevel

class EducationLevelListSerializers(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'

class EducationLevelRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'

class EducationLevelWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'