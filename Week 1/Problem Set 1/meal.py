def main():
    time = input("What time is it now : ").strip().lower()
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# Works for 12 hour format

def convert(time):
    hour, remaining = time.split(":")
    hour = float(hour)
    minute, format = remaining.split(" ")
    if format == "p.m." or format == "p.m"  or format == "pm":
        minute = float(minute)
        minute = minute / 60
        if hour != 12:
            hour = hour + 12
        return hour + minute
    elif format == "a.m." or format == "a.m"  or format == "am":
        minute = float(minute)
        minute = minute / 60
        if hour == 12:
            hour = hour - 12
        return hour + minute

    


if __name__ == "__main__":
    main()