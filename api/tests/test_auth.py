from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

class JWTAuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.token = str(RefreshToken.for_user(self.user).access_token)  # Generate token

    def test_token_generation(self):
        self.assertIsNotNone(self.token)  # Ensure token is generated
