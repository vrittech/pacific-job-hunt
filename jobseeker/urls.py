from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import  jobseeker_viewsets

router = DefaultRouter()

router.register('professional-information', jobseeker_viewsets.ProfessionalInformationViewset, basename="ProfessionalInformationViewset")

urlpatterns = [    
    path('', include(router.urls)),
]