from django.urls import path
from .views import getSample

urlpatterns=[
    path('get-sample-excel/<str:type>/',getSample.as_view(),name="import_excel")
]