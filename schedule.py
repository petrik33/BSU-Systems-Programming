import argparse
from datetime import datetime, timedelta


def generate_schedule(start_time, end_time, name):
    # Define the day names in Russian
    day_names = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

    hours_worked = ((end_time - start_time).seconds / 3600) - 1

    # Get the current date and the next Monday
    today = datetime.today()
    start_date = today + timedelta(days=(7 - today.weekday())) if today.weekday() >= 3 else today + timedelta(days=(0 - today.weekday()))

    # Calculate the end date (always the Sunday of the same week)
    end_date = start_date + timedelta(days=6)

    # Print the header
    print(f"Рабочий график ({name}) {start_date.strftime('%Y.%d.%m')} - {end_date.strftime('%Y.%d.%m')}")

    # Create a dictionary to hold the schedule
    schedule = {}

    # Populate the schedule for each day
    for i in range(7):
        day_date = start_date + timedelta(days=i)
        day_name = day_names[i]

        if i <= 4:
            schedule[day_date.strftime('%Y-%d-%m')] = [start_time.strftime('%H:%M'), "13:00", 4, "14:00", end_time.strftime('%H:%M'), int(hours_worked)]
        else:
            schedule[day_date.strftime('%Y-%d-%m')] = None

    # Print the schedule
    for date, times in schedule.items():
        if times is not None:
            print(f"{day_names[datetime.strptime(date, '%Y-%d-%m').weekday()]}  {date} - {times[0]} - {times[1]}; {times[3]} - {times[4]};  {times[5]}ч")
        else:
            print(f"{day_names[datetime.strptime(date, '%Y-%d-%m').weekday()]}  {date} - ")

    # Print the total hours worked
    print(f"Итого: {hours_worked * 5:.0f}ч")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", help="start time in hh:mm format", type=lambda s: datetime.strptime(s, "%H:%M"))
    parser.add_argument("--end", help="end time in hh:mm format", type=lambda s: datetime.strptime(s, "%H:%M"))
    args = parser.parse_args()

    generate_schedule(args.start, args.end, "Петрикевич Т.Ю.")