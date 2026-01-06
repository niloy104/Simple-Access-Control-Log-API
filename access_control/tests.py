from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import AccessLog
import os
# Create your tests here.
class AccessLogAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.log_file = os.path.join(BASE_DIR, 'system_events.log')
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def _read_log(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return f.read()
        return ""

    def test_create_access_log(self):
        data = {"card_id": "C1001", "door_name": "Main Entrance", "access_granted": True}
        response = self.client.post('/api/logs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        log_content = self._read_log()
        self.assertIn('CREATE: Access log created for card C1001', log_content)

    def test_list_access_logs(self):
        AccessLog.objects.create(card_id="C1001", door_name="Main Entrance", access_granted=True)
        AccessLog.objects.create(card_id="C1002", door_name="Side Door", access_granted=False)
        response = self.client.get('/api/logs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve_access_log(self):
        log = AccessLog.objects.create(card_id="C1001", door_name="Main Entrance", access_granted=True)
        response = self.client.get(f'/api/logs/{log.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_access_log(self):
        log = AccessLog.objects.create(card_id="C1001", door_name="Main Entrance", access_granted=True)
        old_timestamp = log.timestamp
        data = {"card_id": "C1001", "door_name": "Side Door", "access_granted": False}
        response = self.client.put(f'/api/logs/{log.id}/', data, format='json')
        log.refresh_from_db()
        self.assertEqual(log.door_name, "Side Door")
        self.assertFalse(log.access_granted)
        self.assertEqual(log.timestamp, old_timestamp)

    def test_delete_access_log(self):
        log = AccessLog.objects.create(card_id="C1001", door_name="Main Entrance", access_granted=True)
        response = self.client.delete(f'/api/logs/{log.id}/')
        log_content = self._read_log()
        self.assertIn(f'DELETE: Access log (ID: {log.id}) for card C1001', log_content)