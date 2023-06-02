from rest_framework import serializers
from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    fuel_tank_capacity = serializers.ReadOnlyField()
    fuel_consumption_per_minute = serializers.ReadOnlyField()
    max_minutes_able_to_fly = serializers.ReadOnlyField()

    class Meta:
        model = Airplane
        fields = (
            "id",
            "passengers",
            "fuel_tank_capacity",
            "fuel_consumption_per_minute",
            "max_minutes_able_to_fly",
        )

    def validate(self, data):
        if Airplane.objects.count() >= 10:
            raise serializers.ValidationError("Cannot create more than 10 airplanes.")

        return data
