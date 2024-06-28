"""
URL configuration for Pacific project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from company.urls import router as company_routers
from accounts.router import router as accounts_urls
from job.urls import router as job_routers
from jobseeker.urls import router as jobseeker_routers
from professions.urls import router as professioin_routers
from education.urls import router as education_routers
from workexperience.urls import router as workexperience_routers
from jobbookmark.urls import router as jobbookmark_routers
from jobapply.urls import router as jobapply_routers
from socialmedia.urls import router as socialmedia_routers
from resumes.urls import router as resumes_router
from notification.urls import router as notification_router
from jobutils.urls import router as  jobutils_router

router = routers.DefaultRouter()
router.registry.extend(company_routers.registry)
router.registry.extend(accounts_urls.registry)
router.registry.extend(jobseeker_routers.registry)
router.registry.extend(accounts_urls.registry)
router.registry.extend(job_routers.registry)
router.registry.extend(professioin_routers.registry)
router.registry.extend(education_routers.registry)
router.registry.extend(workexperience_routers.registry)
router.registry.extend(jobbookmark_routers.registry)
router.registry.extend(jobapply_routers.registry)
router.registry.extend(socialmedia_routers.registry)
router.registry.extend(resumes_router.registry)
router.registry.extend(notification_router.registry)
router.registry.extend(jobutils_router.registry)

schema_view = get_schema_view(
   openapi.Info(
      title="PACIFIC-JOB-HUNT",
      default_version='v1',
      description="PACIFIC-JOB-HUNT",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="manojdas.py@gmail.com"),
      license=openapi.License(name="No License"),
      **{'x-logo': {'url': 'your-logo-url'}},
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/accounts/',include('accounts.urls')),
    path('api/accounts-management/',include('accountsmanagement.urls')),
    path('job-utils/',include('jobutils.urls')),
    path('reports/',include('report.urls')),
    
   # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
