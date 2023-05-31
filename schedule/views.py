from datetime import datetime

from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer, ServiceProviderSerializer
from schedule.utils import get_available_schedules


# Create your views here.


class IsOwnerOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        username = request.query_params.get("username", None)
        if request.user.username == username:
            return True
        return False


class IsServiceProvider(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.service_provider == request.user:
            return True
        return False


class ScheduleList(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsOwnerOrCreateOnly]

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = Schedule.objects.filter(service_provider__username=username)
        return queryset


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsServiceProvider]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ServiceProviderList(generics.ListAPIView):
    serializer_class = ServiceProviderSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]


@api_view(http_method_names=["GET"])
def get_times(request):
    data = request.query_params.get("data")
    if not data:
        data = datetime.now().date()
    else:
        data = datetime.fromisoformat(data).date()

    available_schedules = sorted(list(get_available_schedules(data)))
    return JsonResponse(available_schedules, safe=False)
