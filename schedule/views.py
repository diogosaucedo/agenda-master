from django.shortcuts import get_object_or_404
from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.
@api_view(http_method_names=["GET", "PATCH"])
def schedule_detail(request, id):
    if request.method == "GET":
        schedule = get_object_or_404(Schedule, id=id)
        serializer = ScheduleSerializer(schedule)
        return JsonResponse(serializer.data)
    if request.method == "PATCH":
        schedule = get_object_or_404(Schedule, id=id)
        serializer = ScheduleSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            schedule.date_time = validated_data.get("date_time", schedule.date_time)
            schedule.custumer_name = validated_data.get(
                "custumer_name", schedule.custumer_name
            )
            schedule.custumer_email = validated_data.get(
                "custumer_email", schedule.custumer_email
            )
            schedule.custumer_phone = validated_data.get(
                "custumer_phone", schedule.custumer_phone
            )
            schedule.save()
            return JsonResponse(validated_data, status=200)
        return JsonResponse(serializer.errors, status=400)


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
            validated_data = serializer.validated_data
            Schedule.objects.create(
                date_time=validated_data["date_time"],
                custumer_name=validated_data["custumer_name"],
                custumer_email=validated_data["custumer_email"],
                custumer_phone=validated_data["custumer_phone"],
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
