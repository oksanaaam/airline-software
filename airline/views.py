from rest_framework.decorators import api_view
from rest_framework.response import Response
from math import log10

from airline.models import Airplane
from airline.serializers import AirplaneSerializer


@api_view(["POST"])
def create_airplanes(request):
    airplanes = []
    total_fuel_consumption = 0
    max_minutes_fly = float("inf")

    for i in range(1, 11):
        id = request.data.get(f"airplane{i}_id")
        passenger_count = request.data.get(f"airplane{i}_passenger_count")

        fuel_tank_capacity = 200 * id
        fuel_consumption = log10(id) * 0.80 + passenger_count * 0.002
        total_fuel_consumption += fuel_consumption
        minutes_fly = fuel_tank_capacity / fuel_consumption
        max_minutes_fly = min(max_minutes_fly, minutes_fly)

        airplane = Airplane(id=id, passenger_count=passenger_count)
        airplanes.append(airplane)

    serializer = AirplaneSerializer(airplanes, many=True)
    return Response({
        "airplanes": serializer.data,
        "total_fuel_consumption_per_minute": total_fuel_consumption,
        "maximum_minutes_able_to_fly": max_minutes_fly,
    })
