from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import education_viewsets,education_level_viewsets

router = DefaultRouter()


router.register('education-information', education_viewsets.EducationViewset, basename="EducationViewset")
router.register('education-level', education_level_viewsets.EducationLevelViewset, basename="EducationLevel")


urlpatterns = [    
    path('', include(router.urls)),
]