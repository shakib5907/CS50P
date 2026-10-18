def main():
    time = input("What time is it now : ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    minute = (minute * 100) / 60
    minute = minute / 100
    return hour + minute


if __name__ == "__main__":
    main()