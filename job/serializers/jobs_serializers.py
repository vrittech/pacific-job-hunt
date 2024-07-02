from rest_framework import serializers
from ..models import Jobs
from company.models import Company
from ..models import JobCategory
from professions.models import Profession


class Profession_PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields =  ['name','id']


class Company_PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields =  ['company_name','company_slug','company_logo','location','type']

class Company_RetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields =  ['company_name','company_slug','company_logo','location','type']

class JobCategory_PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields =  ['name','slug']


class JobCategory_JobRetrieveAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields =  ['name','slug','id']        

class JobListPublicSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    position = Profession_PublicSerializer(read_only = True)
    is_apply = serializers.SerializerMethodField()
    is_save = serializers.SerializerMethodField()

    level = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    timing = serializers.SerializerMethodField()

    def get_level(self,obj):
        try:
            return obj.level.name
        except:
            return ''
    
    def get_timing(self,obj):
        try:
            return obj.timing.name
        except:
            return ''

    def get_location(self,obj):
        try:
            return obj.location.name
        except:
            return ''
    
    class Meta:
        model = Jobs
        fields = '__all__'
    
    def get_is_apply(self,obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.apply_jobs.all().filter(job_id = obj.id).exists()
        return False
    
    def get_is_save(self,obj):
        # return False
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.saved_jobs.all().filter(job_id = obj.id).exists()
        return False
    
class JobListAdminSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_PublicSerializer(read_only = True)
    position = Profession_PublicSerializer(read_only = True)
    number_of_applicant = serializers.SerializerMethodField()
    number_of_saved_applicant = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    timing = serializers.SerializerMethodField()
    
    class Meta:
        model = Jobs
        fields = '__all__'
        
    def get_number_of_applicant(self,obj):
        return obj.number_of_applicant
    
    def get_number_of_saved_applicant(self,obj):
        return obj.number_of_saved_applicant
    
    def get_level(self,obj):
        try:
            return obj.level.name
        except:
            return ''
    
    def get_timing(self,obj):
        try:
            return obj.timing.name
        except:
            return ''

    def get_location(self,obj):
        try:
            return obj.location.name
        except:
            return ''
    
class JobRetrieveAdminSerializer(serializers.ModelSerializer):
    company = Company_PublicSerializer(read_only = True)
    category = JobCategory_JobRetrieveAdminSerializer(read_only = True)
    position = Profession_PublicSerializer(read_only = True)

    level = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    timing = serializers.SerializerMethodField()

    def get_level(self,obj):
        return obj.level.name
    
    def get_timing(self,obj):
        return obj.timing.name

    def get_location(self,obj):
        return obj.location.name
    
    class Meta:
        model = Jobs
        fields = '__all__'

class JobRetrievePublicSerializer(serializers.ModelSerializer):
    company = Company_RetrieveSerializer(read_only = True) #company social media requirement.
    category = JobCategory_PublicSerializer(read_only = True)
    is_apply = serializers.SerializerMethodField()
    is_save = serializers.SerializerMethodField()
    position = Profession_PublicSerializer(read_only = True)

    level = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    timing = serializers.SerializerMethodField()

    def get_level(self,obj):
        return obj.level.name
    
    def get_timing(self,obj):
        return obj.timing.name

    def get_location(self,obj):
        return obj.location.name
    
    class Meta:
        model = Jobs
        fields = '__all__'

    def get_is_apply(self,obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.apply_jobs.all().filter(job_id = obj.id).exists()
        return False
    
    def get_is_save(self,obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return user.saved_jobs.all().filter(job_id = obj.id).exists()
        return False

class JobWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
