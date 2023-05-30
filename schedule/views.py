from rest_framework import generics

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer


# Create your views here.


class ScheduleList(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = Schedule.objects.filter(service_provider__username=username)
        return queryset


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
