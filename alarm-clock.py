import time
from datetime import datetime


alarm_time = input("Enter alarm time (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}...")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("⏰⏰ WAKE UP! It's time!")
        break
    time.sleep(1)
