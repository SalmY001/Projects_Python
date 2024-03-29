# Countdown Timer

# Ideas used from freeCodeCamp, https://www.freecodecamp.org/news/python-sleep-time-sleep-in-python and YouTube, https://www.youtube.com/watch?v=KseiSR0MCTI

from time import sleep

try:
    select_time = int(input("Enter time required in seconds: "))
except ValueError:
    print("Try again, enter integer numbers only.")
else:
    for i in range(select_time, 0, -1):
        seconds = i % 60
        mins = int(i / 60) % 60
        hours = int(i / 3600)
        print(f"{hours:02}: {mins:02}: {seconds:02}", end="\r")
        sleep(1)
    print("Time is over!")
