from datetime import date
import requests


def is_holiday(data: date) -> bool:
    year = data.year
    r = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{year}")

    if r.status_code != 200:
        raise ValueError("It was not possible to consult the holidays")

    holidays = r.json()
    for holiday in holidays:
        date_holiday_as_string = holiday["date"]
        date_holiday = date.fromisoformat(date_holiday_as_string)
        if data == date_holiday:
            return True

    return False
