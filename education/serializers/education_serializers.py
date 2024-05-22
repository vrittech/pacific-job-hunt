from rest_framework import serializers
from ..models import Education

class EducationListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class EducationRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class EducationWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'