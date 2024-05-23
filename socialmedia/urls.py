from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import mysocialmedia_viewsets,social_media_viewsets

router = DefaultRouter()


router.register('my-social-media', mysocialmedia_viewsets.MySocialMediaViewset, basename="MySocialMediaViewset")
router.register('social-media', social_media_viewsets.SocialMediaViewset, basename="SocialMediaViewset")

urlpatterns = [    
    path('', include(router.urls)),
]