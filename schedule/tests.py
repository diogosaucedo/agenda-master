import json

from rest_framework.test import APITestCase


# Create your tests here.
class TestScheduleList(APITestCase):
    """
    To do: add tests for creation, update, detail and delete
    """

    def test_empty_list(self):
        response = self.client.get("/api/schedules/")
        data = json.loads(response.content)
        self.assertEqual(data, [])
