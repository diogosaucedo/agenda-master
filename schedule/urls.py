from django.urls import path

from schedule.views import ScheduleDetail, ScheduleList, ServiceProviderList, get_times

urlpatterns = [
    path("schedules/", ScheduleList.as_view()),
    path("schedules/<int:pk>/", ScheduleDetail.as_view()),
    path("providers/", ServiceProviderList.as_view()),
    path("times/", get_times),
]
