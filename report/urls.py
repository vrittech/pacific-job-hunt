from django.urls import path
from .views import getSample

urlpatterns=[
    path('get-samaple-excel/<str:type>/',getSample.as_view(),name="import_excel")
]