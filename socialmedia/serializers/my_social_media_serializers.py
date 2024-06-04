from rest_framework import serializers
from ..models import MySocialMedia,SocialMedia

class SocialMediaMediaListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class MySocialMediaListSerializers(serializers.ModelSerializer):
    social_media = SocialMediaMediaListSerializers()
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