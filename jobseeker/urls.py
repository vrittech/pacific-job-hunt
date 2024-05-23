from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import  jobseeker_viewsets,jobseeker_have_skills_viewsets

router = DefaultRouter()

router.register('professional-information', jobseeker_viewsets.ProfessionalInformationViewset, basename="ProfessionalInformationViewset")
router.register('jobseeker-have-skills', jobseeker_have_skills_viewsets.JobSeekerHaveSkillsViewset, basename="JobSeekerHaveSkillsViewset")


urlpatterns = [    
    path('', include(router.urls)),
]