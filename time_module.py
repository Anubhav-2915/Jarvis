from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  
    # %I = 12-hour format
    # %M = minutes
    # %p = AM/PM
    return current_time


def get_date():
    today = datetime.now()
    current_date = today.strftime("%A, %d %B %Y")
    # %A = full weekday
    # %d = day
    # %B = month name
    # %Y = year
    return current_date