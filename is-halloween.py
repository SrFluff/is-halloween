import datetime
def is_halloween():
    now = datetime.date.today()
    month = now.month
    day = now.day
    if month == 10 and day == 31:
        return True
    else:
        return False
