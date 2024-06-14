from rest_framework import serializers
from ..models import CustomUser
from jobseeker.models import ProfessionalInformation,Profession

class ProfessionSerializers(serializers.ModelSerializer):
      class Meta:
        ref_name = "ProfessionSerializers"
        model = Profession
        fields = ['name'] 

class ProfessionalInformationSerializers(serializers.ModelSerializer):
      profession = ProfessionSerializers()
      class Meta:
        model = ProfessionalInformation
        fields = ['experience','profession'] 

class JobseekersDetailSerializers(serializers.ModelSerializer):
    professional_information  = ProfessionalInformationSerializers()
    applied_jobs = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','username','created_date','applied_jobs','professional_information'] 

    def get_applied_jobs(self,obj):
        return 12
    

