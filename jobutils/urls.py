from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import job_timing_viewsets,job_level_viewsets,job_location_viewsets
from .views import ImportExel,getSample

router = DefaultRouter()


router.register('job-timing', job_timing_viewsets.JobTimingViewset, basename="JobTimingViewset")
router.register('job-level', job_level_viewsets.JobLevelViewset, basename="JobLevelViewset")
router.register('job-location', job_location_viewsets.JobLocationViewset, basename="JobLocationViewset")

urlpatterns = [    
    # path('', include(router.urls)),
    path('import-excel/<str:type>/',ImportExel.as_view(),name="import_excel"),
    path('get-samaple-excel/<str:type>/',getSample.as_view(),name="import_excel")
]