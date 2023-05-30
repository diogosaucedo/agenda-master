from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer


# Create your views here.


class ScheduleDetail(APIView):
    def get(self, request, id):
        schedule = get_object_or_404(Schedule, id=id)
        serializer = ScheduleSerializer(schedule)
        return JsonResponse(serializer.data)

    def patch(self, request, id):
        schedule = get_object_or_404(Schedule, id=id)
        serializer = ScheduleSerializer(schedule, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id):
        schedule = get_object_or_404(Schedule, id=id)
        schedule.delete()
        return Response(status=204)


class ScheduleList(APIView):
    def get(self, resquest):
        query_set = Schedule.objects.all()
        serializer = ScheduleSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = request.data
        serializer = ScheduleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
