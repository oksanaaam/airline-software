from rest_framework import viewsets
from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
