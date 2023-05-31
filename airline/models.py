from django.db import models


class Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    passenger_count = models.IntegerField()
