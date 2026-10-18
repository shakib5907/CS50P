def main():
    time = input("What time is it now : ").strip().lower()
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hour, remaining = time.split(":")
    hour = float(hour)
    minute, format = remaining.split(" ")
    if format == "p.m.":
        minute = float(minute)
        minute = (minute * 100) / 60
        minute = minute / 100
        hour = hour + 12
        return hour + minute
    elif format == "a.m.":
            minute = float(minute)
            minute = (minute * 100) / 60
            minute = minute / 100
            return hour + minute


if __name__ == "__main__":
    main()