from django.shortcuts import get_object_or_404
from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.
@api_view(http_method_names=["GET"])
def schedule_detail(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    serializer = ScheduleSerializer(schedule)
    return JsonResponse(serializer.data)


@api_view(http_method_names=["GET"])
def schedule_list(request):
    query_set = Schedule.objects.all()
    serializer = ScheduleSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)
