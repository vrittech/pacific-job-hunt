from rest_framework import serializers
from accounts.models import CustomUser
from django.contrib.auth.hashers import make_password

from django.core.cache import cache
from django.db.models import Q

def TokenValidate(token,email,key):
    user = CustomUser.objects.filter(Q(email=email))
    if user.exists():
        user = user.first()
        user.save()
        user_check_key = key+str(user.id)
        token_access = cache.get(user_check_key)
        if token_access == token:
            user.is_verified = True
            return True
    return False
    

class TokenValidationSerializer(serializers.Serializer):
    otp = serializers.CharField()
    email = serializers.CharField()
    
    def validate_otp(self, value):
        # Perform your token validation logic here
        email = self.initial_data.get('email')  # Access email from initial data
        if not TokenValidate(value,email,"password_reset_otp_"):
            raise serializers.ValidationError("Invalid token")
        return value

        
class CustomPasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField(min_length=5)
    password = serializers.CharField(min_length=4)
    email = serializers.CharField()

    class Meta:
        fields = '__all__'

    def validate_password(self, value):
        # Hash the password using Django's make_password function
        return make_password(value)
    
    def validate_token(self, value):
        # Perform your token validation logic here
        email = self.initial_data.get('email')  # Access email from initial data
        if not TokenValidate(value,email,"password_reset_otp_"):
            raise serializers.ValidationError("Invalid token")
        return value
    
    def validate(self, attrs):
        attrs  =  super().validate(attrs)
 
        if TokenValidate(self.initial_data.get('token') ,self.initial_data.get('email'),"password_reset_otp_"):
            attrs['token_validate'] = True
        else:
            attrs['token_validate'] = False
        return attrs
    
class EmailResetSerializer(serializers.Serializer):
    token = serializers.CharField(min_length=5)
    second_email = serializers.EmailField()
    email = serializers.EmailField()

    class Meta:
        fields = '__all__'


    def validate_token(self, value):
        # Perform your token validation logic here
        email = self.initial_data.get('email')  # Access email from initial data
        if not TokenValidate(value,email,"email_reset_otp_"):
            raise serializers.ValidationError("Invalid token")
        return value
    
    def validate(self, attrs):
        attrs  =  super().validate(attrs)
 
        if TokenValidate(self.initial_data.get('token') ,self.initial_data.get('email'),"email_reset_otp_"):
            attrs['token_validate'] = True
        else:
            attrs['token_validate'] = False
        return attrs

 
class EmailNumberSerializer(serializers.Serializer):
    email = serializers.EmailField()

class EmailResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    second_email = serializers.EmailField()


class ContactMeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(required = False)
    message = serializers.CharField()
    phone = serializers.CharField(required = False)
    full_name =  serializers.CharField()

