from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer, ServiceProviderSerializer


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
