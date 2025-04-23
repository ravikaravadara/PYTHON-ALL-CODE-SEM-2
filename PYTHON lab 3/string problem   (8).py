def print_24_hour_clock():
    """Prints the 24 hours of the day with AM/PM, Noon, and Midnight suffixes."""

    for hour in range(24):
        if hour == 0:
            print("12 AM (Midnight)")
        elif hour == 12:
            print("12 PM (Noon)")
        elif 1 <= hour <= 11:
            print(f"{hour} AM")
        elif 13 <= hour <= 23:
            print(f"{hour - 12} PM")


print_24_hour_clock()


# More formatted output (aligned columns):

def print_24_hour_clock_formatted():
    """Prints the 24 hours with aligned columns."""

    for hour in range(24):
        time_str = ""
        if hour == 0:
            time_str = "12 AM (Midnight)"
        elif hour == 12:
            time_str = "12 PM (Noon)"
        elif 1 <= hour <= 11:
            time_str = f"{hour:2} AM"  #:2 for padding (2 spaces)
        elif 13 <= hour <= 23:
            time_str = f"{hour - 12:2} PM"

        print(f"{hour:2}:00 - {time_str}") # Added minutes and aligned hours


print_24_hour_clock_formatted()


# Using datetime module (more robust for time manipulation):

import datetime

def print_24_hour_clock_datetime():
    """Prints 24-hour clock using datetime module."""
    for hour in range(24):
        dt_object = datetime.time(hour=hour) # Create a time object

        if hour == 0:
            print(dt_object.strftime("%I %p (Midnight)")) # strftime for formatting
        elif hour == 12:
            print(dt_object.strftime("%I %p (Noon)"))
        else:
            print(dt_object.strftime("%I %p"))


print("\n--- Using datetime module ---")
print_24_hour_clock_datetime()


#Using datetime module for formatted output

def print_24_hour_clock_datetime_formatted():
    """Prints 24-hour clock using datetime module with formatted output."""
    for hour in range(24):
        dt_object = datetime.time(hour=hour)
        formatted_time = dt_object.strftime("%I:%M %p")  # Include minutes

        if hour == 0:
            print(f"{hour:2}:00 - {formatted_time} (Midnight)")
        elif hour == 12:
            print(f"{hour:2}:00 - {formatted_time} (Noon)")
        else:
            print
