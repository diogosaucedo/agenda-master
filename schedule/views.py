from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer


# Create your views here.


class ScheduleList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get(self, resquest, *args, **kwargs):
        return self.list(resquest, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ScheduleDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
