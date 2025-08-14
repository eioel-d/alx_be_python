from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    return datetime.now()

current_date = display_current_datetime().strftime("%Y-%m-%d %H:%M:%S")

print(f"Current date and time: {current_date}")
no_of_days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date = display_current_datetime() + timedelta(days = no_of_days)
calculate_future_date = calculate_future_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"Future date: {calculate_future_date}")
