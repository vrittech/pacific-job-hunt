from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import job_timing_viewsets,job_level_viewsets,job_location_viewsets,education_level_viewsets

router = DefaultRouter()


router.register('job-timing', job_timing_viewsets.JobTimingViewset, basename="JobTimingViewset")
router.register('job-level', job_level_viewsets.JobLevelViewset, basename="JobLevelViewset")
router.register('job-location', job_location_viewsets.JobLocationViewset, basename="JobLocationViewset")
router.register('education-level', education_level_viewsets.EducationLevelViewset, basename="EducationLevel")
urlpatterns = [    
    path('', include(router.urls)),
]