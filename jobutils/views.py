from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd

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
        return Response({"message": "File processed successfully"}, status=status.HTTP_201_CREATED)