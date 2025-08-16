import random
from datetime import datetime, timedelta

def generate_random_datetime(start_date, end_date):
    """
    Generates a random datetime object between a given start and end date.

    Args:
        start_date (datetime): The starting datetime.
        end_date (datetime): The ending datetime.

    Returns:
        datetime: A randomly generated datetime object.
    """
    time_between_dates = end_date - start_date
    total_seconds = time_between_dates.total_seconds()
    random_seconds = random.randint(0, int(total_seconds))
    random_datetime = start_date + timedelta(seconds=random_seconds)

    return random_datetime
start_dt_str = "2023-01-01 00:00:00"
end_dt_str = "2024-12-31 23:59:59"
start_dt = datetime.strptime(start_dt_str, "%Y-%m-%d %H:%M:%S")
end_dt = datetime.strptime(end_dt_str, "%Y-%m-%d %H:%M:%S")
random_date_time = generate_random_datetime(start_dt, end_dt)
print("Generated random date and time:", random_date_time)