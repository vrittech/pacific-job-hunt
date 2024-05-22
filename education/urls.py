from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import education_viewsets

router = DefaultRouter()


router.register('education-information', education_viewsets.EducationViewset, basename="EducationViewset")

urlpatterns = [    
    path('', include(router.urls)),
]