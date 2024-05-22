from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import jobseeker_saved_jobs_viewsets

router = DefaultRouter()

router.register('jobseeker-saved-jobs', jobseeker_saved_jobs_viewsets.JobSeekerHaveSavedJobsViewSets, basename="JobSeekerHaveSavedJobsViewSets")

urlpatterns = [    
    path('', include(router.urls)),
]