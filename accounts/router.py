from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import LoginView
from rest_framework.routers import DefaultRouter
from .views import PermissionAllDelete,RoleViewSet,CheckTokenExpireView,userLimitedData,AllUserData
from .group_permission import PermissionHasGroupViewSet,CustomPermissionInsert

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()

router.register('users', views.CustomUserSerializerViewSet, basename="CustomUserSerializer")
