from django.urls import path

from schedule.views import ScheduleDetail, ScheduleList

urlpatterns = [
    path("schedules/", ScheduleList.as_view()),
    path("schedules/<int:pk>/", ScheduleDetail.as_view()),
]
