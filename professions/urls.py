from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import professioin_viewsets

router = DefaultRouter()


router.register('profession', professioin_viewsets.ProfessionViewSets, basename="ProfessionViewSets")

urlpatterns = [    
    path('', include(router.urls)),
]