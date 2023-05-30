from django.urls import path

from schedule.views import schedule_detail, schedule_list

urlpatterns = [
    path("schedules/", schedule_list),
    path("schedules/<int:id>/", schedule_detail),
]
