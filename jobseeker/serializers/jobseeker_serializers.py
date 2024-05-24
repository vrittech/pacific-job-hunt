from rest_framework import serializers
from ..models import ProfessionalInformation
from job.models import JobCategory
from professions.models import Profession

import ast

def str_to_list(data,value_to_convert):
    mutable_data = data.dict()
    value_to_convert_data = mutable_data[value_to_convert]
    if type(value_to_convert_data) == list:
        return mutable_data
    try:
        variations = ast.literal_eval(value_to_convert_data)
        mutable_data[value_to_convert] = variations
        return mutable_data
    except ValueError as e:
        raise serializers.ValidationError({f'{value_to_convert}': str(e)})


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

    def to_internal_value(self, data):
        if data.get('interest'):
            data = str_to_list(data,'interest')
            return super().to_internal_value(data)
        return super().to_internal_value(data)

    class Meta:
        model = ProfessionalInformation
        fields = '__all__'