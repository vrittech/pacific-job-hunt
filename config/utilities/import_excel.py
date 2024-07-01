from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
import csv

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from job.models import JobCategory,Skills
from professions.models import  Profession
from company.models import CompanyType

from job.serializers.job_category_serializers import JobCategoryWriteSerializers
from job.serializers.skills_serializers import SkillsWriteSerializers
from professions.serializers.profession_serializers import ProfessionWriteSerializers
from company.serializers.company_type_serializers import CompanyTypeWriteSerializers


# Create your views here.

class ImportExel(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'excel_file': openapi.Schema(type=openapi.TYPE_FILE),
            },
            required=['excel_file']
        ),
        # responses={200: MyResponseSerializer},
        operation_summary="upload excel file",
        operation_description="upload excel file",
    )
    def post(self, request, type, format=None):
       
        file = request.FILES.get('excel_file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        # Use pandas to read the Excel file
        df = pd.read_csv(file)

        # Convert the DataFrame to a list of dictionaries
        datas = df.to_dict(orient='records')
        # Process the DataFrame based on the 'type' parameter

        if type == "job-category":
            create_update(JobCategory,JobCategoryWriteSerializers,datas,'name')
        elif type == "profession":
            create_update(Profession,ProfessionWriteSerializers,datas,'name')
        elif type == "skills":
            create_update_skills(Skills,SkillsWriteSerializers,datas,'name')
        elif type == "company-type":
            create_update(CompanyType,CompanyTypeWriteSerializers,datas,'type')
        else:
            return Response({"message": 'Unknown file type'}, status=status.HTTP_400_BAD_REQUEST)
        

        return Response({"message": "File processed successfully"}, status=status.HTTP_201_CREATED)
        # except Exception as e:
        #      return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

def create_update(my_model,my_serializer,datas,unique_field_name):
    
    for record in datas:
        existing_data = my_model.objects.filter(name=record[unique_field_name])
        if existing_data.exists():
            existing_data = existing_data.first()  # Use a unique field here
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
                pass


def create_update_skills(my_model,my_serializer,datas,unique_field_name):
    
    for record in datas:
        existing_data = my_model.objects.filter(name=record[unique_field_name])
        if existing_data.exists():
            existing_data = existing_data.first()  # Use a unique field here
            if record.get('category'):
                category_obj = JobCategory.objects.filter(name = record.get('category'))
                if category_obj.exists:
                    category_obj = category_obj.first()
                    record['category'] = category_obj
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
                pass
