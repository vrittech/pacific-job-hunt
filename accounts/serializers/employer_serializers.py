from rest_framework import serializers
from ..models import CustomUser
from company.models import Company,CompanyType
from socialmedia.models import CompanySocialMedia,SocialMedia

class CompanySocialMediaSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "accountsCompanySerializers"
        model = SocialMedia
        fields = ['id', 'name','image']

class CompanySocialMediaSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "accountsCompanySerializers"
        model = CompanySocialMedia
        fields = ['id', 'url','social_media']

class CompanyTypeSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "accountsCompanySerializers"
        model = CompanyType
        fields = ['id', 'type','slug']

class CompanySerializers(serializers.ModelSerializer):
    type = CompanyTypeSerializers(many=True)
    company_social_media = CompanySocialMediaSerializers(many=True)
    class Meta:
        ref_name = "accountsCompanySerializers"
        model = Company
        fields = ['id', 'company_name','created_date', 'company_slug', 'type', 'email','company_logo','company_banner','is_verified','company_size','company_social_media']

   
class EmployerDetailSerializers(serializers.ModelSerializer):
    my_companies = CompanySerializers(many = True)
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','username','my_companies','is_verified','created_date'] 