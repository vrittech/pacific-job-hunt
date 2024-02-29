from rest_framework import serializers
from ..models import Skills

class SkillsReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class SkillsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'