from rest_framework import serializers
from ..models import ProfessionalInformation
from job.models import JobCategory
from professions.models import Profession


class InterestSerializers_JobSeekerPublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'

class ProfessionSerializers_JobSeekerPublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class JobSeekerListSerializers(serializers.ModelSerializer):
    interest = InterestSerializers_JobSeekerPublicSerializers(many=True,read_only = True)
    profession = ProfessionSerializers_JobSeekerPublicSerializers(read_only = True)
    
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'

class JobSeekerRetrieveSerializers(serializers.ModelSerializer):
    interest = InterestSerializers_JobSeekerPublicSerializers(many=True,read_only = True)
    profession = ProfessionSerializers_JobSeekerPublicSerializers(read_only = True)
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'


class JobSeekerWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalInformation
        fields = '__all__'