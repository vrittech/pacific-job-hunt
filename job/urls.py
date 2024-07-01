from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import job_caategory_viewsets, jobs_viewsets,skills_viewsets

router = DefaultRouter()

router.register('job-category', job_caategory_viewsets.JobsCategoryViewSets, basename="JobsCategoryViewSets")
router.register('jobs', jobs_viewsets.JobViewSets, basename="JobViewSets")
router.register('skills', skills_viewsets.SkillsViewSets, basename="SkillsViewSets")

urlpatterns = [    
    path('', include(router.urls)),
]
