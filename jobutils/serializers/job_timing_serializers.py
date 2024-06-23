from rest_framework import serializers
from ..models import JobTiming

class JobTimingListSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobTiming
        fields = '__all__'

class JobTimingRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobTiming
        fields = '__all__'

class JobTimingWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobTiming
        fields = '__all__'