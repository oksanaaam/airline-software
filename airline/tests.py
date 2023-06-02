from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Airplane

AIRPLANE_URL = reverse("airline:airplane-list")


class AirplaneAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_airplane(self):
        data = {"id": 1, "passengers": 50}

        response = self.client.post(AIRPLANE_URL, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 1)
        self.assertEqual(Airplane.objects.get().id, 1)
        self.assertEqual(Airplane.objects.get().passengers, 50)
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["passengers"], 50)
        self.assertEqual(response.data["fuel_tank_capacity"], 200)
        self.assertAlmostEqual(response.data["fuel_consumption_per_minute"], 0.1)
        self.assertAlmostEqual(response.data["max_minutes_able_to_fly"], 2000)

    def test_retrieve_airplanes(self):
        airplane1 = Airplane.objects.create(id=1, passengers=50)
        airplane2 = Airplane.objects.create(id=2, passengers=75)

        response = self.client.get(AIRPLANE_URL, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], airplane1.id)
        self.assertEqual(response.data[0]["passengers"], airplane1.passengers)
        self.assertEqual(response.data[0]["fuel_tank_capacity"], 200)
        self.assertAlmostEqual(response.data[0]["fuel_consumption_per_minute"], 0.1)
        self.assertAlmostEqual(response.data[0]["max_minutes_able_to_fly"], 2000)
        self.assertEqual(response.data[1]["id"], airplane2.id)
        self.assertEqual(response.data[1]["passengers"], airplane2.passengers)
        self.assertEqual(response.data[1]["fuel_tank_capacity"], 400)
        self.assertAlmostEqual(response.data[1]["fuel_consumption_per_minute"], 0.7045177444479562)
        self.assertAlmostEqual(response.data[1]["max_minutes_able_to_fly"], 567.7642659141691)


    def test_delete_airplane(self):
        airplane = Airplane.objects.create(id=1, passengers=50)

        url = reverse("airline:airplane-detail", args=[airplane.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Airplane.objects.count(), 0)
