# return the 4th thursday of the month in a datetime.date object
import datetime


def meetup_date(year, month, *, nth = 4, weekday = 3):
    day_of_month = 1
    # .weekday returns an int 0-6 with monday being 0
    while datetime.datetime(year, month, day_of_month).weekday() != weekday:
        day_of_month += 1

    while (day_of_month - 1) // 7 + 1 != nth:
        day_of_month += 7

    return datetime.date(year, month, day_of_month)


def main():
    print(meetup_date(2015, 8))
    meetup_date(2015, 9)
    meetup_date(2015, 10)
    meetup_date(2016, 1)
    meetup_date(2016, 2)


if __name__ == "__main__":
    main()
