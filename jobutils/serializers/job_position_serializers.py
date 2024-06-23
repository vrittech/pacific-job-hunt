from rest_framework import serializers
from ..models import JobPosition

class JobPositionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'

class JobPositionRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'

class JobPositionWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'