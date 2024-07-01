from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
import csv
from jobutils.models import JobTiming,JobLocation,JobLevel
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers.job_level_serializers import JobLevelWriteSerializers
from .serializers.job_location_serializers import JobLocationWriteSerializers
from .serializers.job_timing_serializers import JobTimingWriteSerializers


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
        
        try:
            # Use pandas to read the Excel file
            df = pd.read_csv(file)

            # Convert the DataFrame to a list of dictionaries
            datas = df.to_dict(orient='records')

            # Process the DataFrame based on the 'type' parameter
            if type == "job-timing": 
                create_update(JobTiming,JobTimingWriteSerializers,datas)
            elif type == "job-level":
                create_update(JobTiming,JobLevelWriteSerializers,datas)
            elif type == "job-location":
                create_update(JobTiming,JobLocationWriteSerializers,datas)
            else:
                return Response({"message": 'Unknown file type'}, status=status.HTTP_400_BAD_REQUEST)
            

            return Response({"message": "File processed successfully", "data": datas}, status=status.HTTP_201_CREATED)
        except Exception as e:
             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

def create_update(my_model,my_serializer,datas):
    for record in datas:
        try:
            existing_data = my_model.objects.get(id=record['id'])  # Use a unique field here
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass
        except my_model.DoesNotExist:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass
