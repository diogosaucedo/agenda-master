from rest_framework import serializers
from schedule.models import Schedule


class ScheduleSerializer(serializers.Serializer):
    date_time = serializers.DateTimeField()
    custumer_name = serializers.CharField(max_length=255)
    custumer_email = serializers.EmailField()
    custumer_phone = serializers.CharField(max_length=20)

    def create(self, validated_data):
        schedule = Schedule.objects.create(
            date_time=validated_data["date_time"],
            custumer_name=validated_data["custumer_name"],
            custumer_email=validated_data["custumer_email"],
            custumer_phone=validated_data["custumer_phone"],
        )
        return schedule

    def update(self, instance, validated_data):
        instance.date_time = validated_data.get("date_time", instance.date_time)
        instance.custumer_name = validated_data.get(
            "custumer_name", instance.custumer_name
        )
        instance.custumer_email = validated_data.get(
            "custumer_email", instance.custumer_email
        )
        instance.custumer_phone = validated_data.get(
            "custumer_phone", instance.custumer_phone
        )
        instance.save()
        return instance
