from django.shortcuts import get_object_or_404
from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(http_method_names=["GET", "PATCH", "DELETE"])
def schedule_detail(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    if request.method == "GET":
        serializer = ScheduleSerializer(schedule)
        return JsonResponse(serializer.data)
    if request.method == "PATCH":
        serializer = ScheduleSerializer(schedule, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        schedule.delete()
        return Response(status=204)


@api_view(http_method_names=["GET", "POST"])
def schedule_list(request):
    if request.method == "GET":
        query_set = Schedule.objects.all()
        serializer = ScheduleSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = request.data
        serializer = ScheduleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
