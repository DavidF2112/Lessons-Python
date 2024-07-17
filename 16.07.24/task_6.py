from datetime import datetime, timedelta

def date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 10)

for single_date in date_range(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))
