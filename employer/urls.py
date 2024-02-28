from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import employer_viewsets,employer_have_jobs_viewsets

router = DefaultRouter()

router.register('employer', employer_viewsets.EmployerViewSets, basename="EmployerViewSets")
router.register('employers-jobs-apply', employer_have_jobs_viewsets.EmployerHaveJobsViewSets, basename="EmployerHaveJobsViewSets")

urlpatterns = [    
    path('', include(router.urls)),
]