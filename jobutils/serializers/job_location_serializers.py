from rest_framework import serializers
from ..models import JobLocation

class JobLocationListSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = '__all__'

class JobLocationRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = '__all__'

class JobLocationWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = '__all__'