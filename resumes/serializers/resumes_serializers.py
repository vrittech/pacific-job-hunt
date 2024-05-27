from rest_framework import serializers
from ..models import Resumes

class ResumesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = '__all__'

class ResumesRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = '__all__'

class ResumesWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = '__all__'