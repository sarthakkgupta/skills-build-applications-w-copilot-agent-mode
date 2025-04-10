from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import User, Team, Activity, Leaderboard, Workout

class BasicTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "pass1234"
        }
        # Create a user to test GET, etc.
        self.user = User.objects.create(**self.user_data)

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that API endpoints are listed
        self.assertIn('users', response.data)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class UserTests(APITestCase):
    def test_create_user(self):
        data = {"username": "testuser", "email": "testuser@example.com", "password": "password123"}
        response = self.client.post("/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        data = {"name": "Test Team"}
        response = self.client.post("/teams/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {"user": user.id, "activity_type": "Running", "duration": 30}
        response = self.client.post("/activities/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {"user": user.id, "score": 100}
        response = self.client.post("/leaderboard/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        data = {"name": "Test Workout", "description": "Test Description"}
        response = self.client.post("/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)