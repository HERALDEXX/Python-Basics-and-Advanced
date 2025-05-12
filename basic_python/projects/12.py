'''Create a python function that tells the current time and date each time you call it'''

from datetime import datetime

def current_time_and_date():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

print(current_time_and_date())
