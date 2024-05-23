from rest_framework import serializers
from ..models import JobSeekerHaveSkills
from job.models import JobCategory
from professions.models import Profession



class JobSeekerHaveSkillsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerHaveSkills
        fields = '__all__'

class JobSeekerHaveSkillsRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerHaveSkills
        fields = '__all__'


class JobSeekerHaveSkillsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerHaveSkills
        fields = '__all__'