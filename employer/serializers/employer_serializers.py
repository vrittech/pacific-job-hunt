from rest_framework import serializers
from ..models import Employer

class EmployerReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

class EmployerWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'