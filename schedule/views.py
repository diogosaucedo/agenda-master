from django.shortcuts import get_object_or_404
from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer
from django.http import JsonResponse


# Create your views here.
def schedule_detail(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    serializer = ScheduleSerializer(schedule)
    return JsonResponse(serializer.data)
