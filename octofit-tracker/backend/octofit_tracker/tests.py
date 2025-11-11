from django.test import TestCase
from rest_framework.test import APIClient


class BasicAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_team_create_and_list(self):
        # Create a team via API
        resp = self.client.post('/teams/', {'name': 'Test Team', 'description': 'desc'}, format='json')
        self.assertIn(resp.status_code, (200, 201))

        # List teams
        list_resp = self.client.get('/teams/')
        self.assertEqual(list_resp.status_code, 200)
        data = list_resp.json()
        self.assertTrue(isinstance(data, list))
        self.assertGreaterEqual(len(data), 1)
