from datetime import datetime, timedelta


def format_calendar_date(date_offset=0):
    # Current date and time
    current_date = datetime.now()

    # Calculate the target date
    target_date = current_date + timedelta(days=date_offset)

    # Format the date
    formatted_date = target_date.strftime('%a, %d %b %Y')

    return formatted_date


def get_today_calendar_date():
    return format_calendar_date()


def get_tomorrow_calendar_date():
    return format_calendar_date(date_offset=1)
