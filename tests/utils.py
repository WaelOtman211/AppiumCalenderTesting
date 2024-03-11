from datetime import datetime, timedelta



def get_today_date_in_calendar_format():
    # Current date and time
    now = datetime.now()

    # Format the date
    formatted_date = now.strftime('%a, %d %b %Y')

    return formatted_date

def get_tomorrow_date_in_calendar_format():
    # Current date and time
    now = datetime.now()

    # Tomorrow's date
    tomorrow = now + timedelta(days=1)

    # Format the date
    formatted_date = tomorrow.strftime('%a, %d %b %Y')

    return formatted_date