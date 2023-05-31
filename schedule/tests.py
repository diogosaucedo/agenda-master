from datetime import datetime, timezone

from rest_framework.test import APITestCase

from unittest import mock


# Create your tests here.
class TestScheduleList(APITestCase):
    """
    To do: add tests for creation, update, detail and delete
    """

    # Must be authenticated before
    # def test_empty_list(self):
    #     response = self.client.get("/api/schedules/")
    #     data = json.loads(response.content)
    #     self.assertEqual(data, [])


class TestGetHorarios(APITestCase):
    """
    TODO: Tests is crashing, fix it later.
    """

    # @mock.patch("schedule.libs.brasil_api.is_holiday", return_value=True)
    # def test_when_date_is_holiday_return_empty_list(self, _):
    #     response = self.client.get("/api/times/?data=2023-12-25")
    #     print("RESPONSE: ", response)
    #     self.assertEqual(response.data, [])

    # @mock.patch("schedule.libs.brasil_api.is_holiday", return_value=False)
    # def test_when_date_is_workday_return_times_list(self, _):
    #     response = self.client.get("/api/times/?data=2023-12-20")
    #     self.assertNotEqual(response.data, [])
    #     self.assertEqual(
    #         response.data[0], datetime(2022, 10, 20, 3, 9, tzinfo=timezone.utc)
    #     )
    #     self.assertEqual(
    #         response.data[-1], datetime(2022, 10, 20, 17, 30, tzinfo=timezone.utc)
    #     )
