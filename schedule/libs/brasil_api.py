from datetime import date
import logging
from django.conf import settings

import requests


def is_holiday(data: date) -> bool:
    logging.info(f"Making a request to BrasilAPI for the date: {data.isoformat()}")
    if settings.TESTING:
        if date.day == 25 and date.month == 12:
            return True
        return False

    year = data.year
    r = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{year}")

    if r.status_code != 200:
        logging.error("An error occurred in Brazil API")
        return False
        # raise ValueError("It was not possible to consult the holidays")

    holidays = r.json()
    for holiday in holidays:
        date_holiday_as_string = holiday["date"]
        date_holiday = date.fromisoformat(date_holiday_as_string)
        if data == date_holiday:
            return True

    return False
