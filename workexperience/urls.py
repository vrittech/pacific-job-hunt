from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import work_experience_viewsets

router = DefaultRouter()

router.register('work-information', work_experience_viewsets.WorkExprienceViewset, basename="WorkExprienceViewset")

urlpatterns = [    
    path('', include(router.urls)),
]