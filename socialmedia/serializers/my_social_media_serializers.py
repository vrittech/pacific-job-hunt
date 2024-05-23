from rest_framework import serializers
from ..models import MySocialMedia

class MySocialMediaListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MySocialMedia
        fields = '__all__'

class MySocialMediaRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = MySocialMedia
        fields = '__all__'

class MySocialMediaWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = MySocialMedia
        fields = '__all__'