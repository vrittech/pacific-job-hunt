from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import jobseekers_have_cv_viewsets

router = DefaultRouter()


router.register('jobseekers-have-resumes', jobseekers_have_cv_viewsets.ResumesViewset, basename="ResumesViewsets")

urlpatterns = [    
    path('', include(router.urls)),
]