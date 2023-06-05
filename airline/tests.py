from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Airplane
from .serializers import AirplaneSerializer

AIRPLANE_URL = reverse("airline:airplane-list")


class AirplaneAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_airplane(self):
        data = {"id": 1, "passengers": 50}

        response = self.client.post(AIRPLANE_URL, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 1)

        airplane = Airplane.objects.get()
        serializer_data = AirplaneSerializer(airplane).data

        self.assertEqual(response.data, serializer_data)

    def test_retrieve_airplanes(self):
        airplane1 = Airplane.objects.create(id=1, passengers=50)
        airplane2 = Airplane.objects.create(id=2, passengers=75)

        response = self.client.get(AIRPLANE_URL, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        serializer1 = AirplaneSerializer(airplane1)
        serializer2 = AirplaneSerializer(airplane2)

        self.assertEqual(response.data[0], serializer1.data)
        self.assertEqual(response.data[1], serializer2.data)

    def test_delete_airplane(self):
        airplane = Airplane.objects.create(id=1, passengers=50)

        url = reverse("airline:airplane-detail", args=[airplane.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Airplane.objects.count(), 0)
