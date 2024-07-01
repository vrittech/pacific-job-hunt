from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
from django.http import HttpResponse
import csv
from jobutils.models import JobTiming,JobLocation,JobLevel

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
            response['Content-Disposition'] = f'attachment; filename="{type}.csv"'

            writer = csv.writer(response)

            # Write the header row
            writer.writerow(['id','name','created_date'])

            # Write data rows
            for data in queryset:
                data_lists = [data.id,data.name,data.created_date]
                writer.writerow(data_lists)

            return response