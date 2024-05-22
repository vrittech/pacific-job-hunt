from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import jobseeker_have_jobs_viewsets, jobseeker_viewsets,jobseeker_saved_jobs_viewsets

router = DefaultRouter()

router.register('professional-information', jobseeker_viewsets.ProfessionalInformationViewset, basename="ProfessionalInformationViewset")
router.register('jobseeker-jobs-apply', jobseeker_have_jobs_viewsets.JobSeekerHaveJobsViewSets, basename="JobSeekerHaveJobsViewSets")
router.register('jobseeker-saved-jobs', jobseeker_saved_jobs_viewsets.JobSeekerHaveSavedJobsViewSets, basename="JobSeekerHaveSavedJobsViewSets")

urlpatterns = [    
    path('', include(router.urls)),
]