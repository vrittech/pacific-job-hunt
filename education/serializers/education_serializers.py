from rest_framework import serializers
from ..models import Education

class EducationListPublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class EducationRetrievePublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class EducationListAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class EducationRetrieveAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class EducationWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'