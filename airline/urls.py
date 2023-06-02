from django.contrib import admin
from django.urls import path, include
from .views import AirplaneViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"airplanes", AirplaneViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
