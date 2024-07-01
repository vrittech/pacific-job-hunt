from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import company_type_viewsets,company_viewsets
from config.utilities.import_excel import ImportExel

router = DefaultRouter()

router.register('company-type', company_type_viewsets.CompanytypeViewSets, basename="CompanytypeViewSets")
router.register('company', company_viewsets.CompanyViewSets, basename="CompanyViewSets")

urlpatterns = [    
    path('import-excel/<str:type>/',ImportExel.as_view(),name="import_excel"),
]