from typing import Iterable
from datetime import date, datetime, timedelta, timezone

from schedule.models import Schedule
from schedule.libs import brasil_api


def get_available_schedules(data: date) -> Iterable[datetime]:
    try:
        if brasil_api.is_holiday(data):
            return []
    except ValueError:
        ...

    start = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=9,
        minute=0,
        tzinfo=timezone.utc,
    )

    end = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=18,
        minute=0,
        tzinfo=timezone.utc,
    )

    delta = timedelta(minutes=30)

    avaliable_schedules = set()

    while start < end:
        if not Schedule.objects.filter(date_time=start).exists():
            avaliable_schedules.add(start)
        start = start + delta

    return avaliable_schedules
