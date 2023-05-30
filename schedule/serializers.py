from rest_framework import serializers
from django.utils import timezone

from schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "date_time",
            "custumer_name",
            "custumer_email",
            "custumer_phone",
        ]

    # Validates only a field
    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "Date time must be greater than current date"
            )
        return value

    # research about it later
    # def validate(self, attrs): Validate all fields. Allows complex validations
