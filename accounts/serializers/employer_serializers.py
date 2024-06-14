from rest_framework import serializers
from ..models import CustomUser



class EmployerDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','username'] 