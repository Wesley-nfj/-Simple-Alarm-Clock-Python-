import time
from datetime import datetime


alarm_time = input("Enter alarm time (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}...")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("⏰⏰ WAKE UP! It's time!")
        break

     alarm = datetime.strptime(alarm_time, "%H:%M:%S")
    seconds_left = int((alarm - now.replace(year=alarm.year, month=alarm.month, day=alarm.day)).total_seconds())

    if seconds_left > 0:
        print(f"{seconds_left} seconds left...", end="\r")
    time.sleep(1)
