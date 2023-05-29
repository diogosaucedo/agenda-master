from rest_framework import serializers


class ScheduleSerializer(serializers.Serializer):
    date_time = serializers.DateTimeField()
    custumer_name = serializers.CharField(max_length=255)
    custumer_email = serializers.EmailField()
    custumer_phone = serializers.CharField(max_length=20)
