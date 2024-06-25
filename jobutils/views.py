from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
import csv
from jobutils.models import JobTiming,JobLocation,JobLevel

# Create your views here.

class ImportExel(APIView):
    def post(self, request, type, format=None):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Use pandas to read the Excel file
            df = pd.read_excel(file)

            # Process the DataFrame based on the 'type' parameter
            if type == 'some_type':
                # Do something with df
                pass
            else:
                # Handle other types or raise an error
                pass

            # Convert the DataFrame to a list of dictionaries
            data = df.to_dict(orient='records')

            return Response({"message": "File processed successfully", "data": data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class getSample(APIView):
    def get(self, request, type, format=None):
            
            if type == "job-timing":
                queryset = JobTiming.objects.all()
            elif type == "job-level":
                queryset = JobLevel.objects.all()
            elif type == "job-location":
                queryset = JobLocation.objects.all()
            else:
                return Response({"message": 'Unknown type'}, status=status.HTTP_400_BAD_REQUEST)
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="rows_export.csv"'

            writer = csv.writer(response)

            # Write the header row
            writer.writerow(['id','name','created_date'])

            # Write data rows
            for data in queryset:
                data_lists = [data.id,data.name,data.created_date]
                writer.writerow(data_lists)

            return response