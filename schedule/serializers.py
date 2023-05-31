from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers

from schedule.models import Schedule
from schedule.utils import get_available_schedules


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "service_provider",
            "date_time",
            "custumer_name",
            "custumer_email",
            "custumer_phone",
        ]

    """
    Validations steps:
    1. Check if types are allowed
    2. Run the field validation, ex: validate_field()
    3. Run the general validation (object-level)
    """

    # Allow string instead of integer, integer is default
    service_provider = serializers.CharField()

    # Validates only a field
    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "Date time must be greater than current date"
            )
        if value not in get_available_schedules(value.date()):
            raise serializers.ValidationError("This time is not available!")
        return value

    def validate_service_provider(self, value):
        try:
            service_provider = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Service provider does not exist")
        return service_provider

    # research about it later
    # def validate(self, attrs)


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "schedules",
        ]

    # Serializing the schedules, PKs to objects
    schedules = ScheduleSerializer(many=True, read_only=True)
