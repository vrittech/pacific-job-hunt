from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', views.CustomUserSerializerViewSet, basename="CustomUserSerializer")
