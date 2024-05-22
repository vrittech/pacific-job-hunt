from rest_framework import serializers
from ..models import Profession

class ProfessionReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

class ProfessionWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'