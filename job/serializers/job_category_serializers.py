from rest_framework import serializers
from ..models import JobCategory

class JobCategoryReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'

class JobCategoryWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'