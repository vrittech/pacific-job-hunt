from rest_framework import serializers
from ..models import Jobs

class JobReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class JobWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'