from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import job_timing_viewsets

router = DefaultRouter()


router.register('education-information', job_timing_viewsets.EducationViewset, basename="EducationViewset")

urlpatterns = [    
    path('', include(router.urls)),
]