from rest_framework import serializers
from ..models import ProfessionalInformation

class JobSeekerListPublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'

class JobSeekerRetrievePublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'

class JobSeekerListAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'

class JobSeekerRetrieveAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'

class JobSeekerWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'