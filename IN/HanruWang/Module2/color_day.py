import datetime
import calendar


def color_of_mybirthday(date):

    born = datetime.datetime.strptime(date, "%m%d%Y").weekday()
    day = calendar.day_name[born]
    color = ""
    if day == "Sunday":
        color = "Red"
    elif day == "Monday":
        color = "Yellow"
    elif day == "Tuseday":
        color = "Pink"
    elif day == "Wednesday":
        color = "Green"
    elif day == "Thursday":
        color = "Orange"
    elif day == "Friday":
        color = "Blue"
    elif day == "Saturday":
        color = "Purple"
    return (day, color)

date = input("What is your birthday? (mm/dd/YYYY): ")
day1, color1 = color_of_mybirthday(date)
print("Color of My Birthday({}): {})".format(day1, color1))


