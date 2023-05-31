from django.urls import path
from .views import create_airplanes

urlpatterns = [
    path("airplanes/", create_airplanes, name="create_airplanes"),
]
