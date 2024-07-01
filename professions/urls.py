from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import professioin_viewsets
from config.utilities.import_excel import ImportExel

router = DefaultRouter()


router.register('profession', professioin_viewsets.ProfessionViewSets, basename="ProfessionViewSets")

urlpatterns = [    
    path('', include(router.urls)),
    path('import-excel/<str:type>/',ImportExel.as_view(),name="import_excel"),
]
