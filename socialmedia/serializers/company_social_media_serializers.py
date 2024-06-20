from rest_framework import serializers
from ..models import CompanySocialMedia,SocialMedia

class SocialMediaMediaListSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "companySocialMediaSerializers"
        model = SocialMedia
        fields = '__all__'

class CompanySocialMediaListSerializers(serializers.ModelSerializer):
    social_media = SocialMediaMediaListSerializers()
    class Meta:
        model = CompanySocialMedia
        fields = '__all__'

class CompanySocialMediaRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanySocialMedia
        fields = '__all__'

class CompanySocialMediaWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanySocialMedia
        fields = '__all__'