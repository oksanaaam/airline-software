import math

from django.db import models


class Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    passengers = models.IntegerField()

    def fuel_tank_capacity(self):
        return self.id * 200

    def fuel_consumption_per_minute(self):
        return math.log(self.id) * 0.80 + (self.passengers * 0.002)

    def max_minutes_able_to_fly(self):
        return self.fuel_tank_capacity() / self.fuel_consumption_per_minute()
