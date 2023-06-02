from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirplaneViewSet

router = DefaultRouter()
router.register("airplanes", AirplaneViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

app_name = "airline"
