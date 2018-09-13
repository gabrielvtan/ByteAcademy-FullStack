import datetime
today = datetime.datetime.now()

def age_to_time(age):
    age = int(age)
    months = 12 * age
    days = 360 * age
    hours = days * 24
    minutes = hours * 60
    return ("months: {}, days: {}, hours: {}, and minutes: {}".format(months, days, hours, minutes))
    

def birthday_to_time(birthday):
    birthday = birthday.split('-')
    days = (today - datetime.datetime(int(birthday[0]), int(birthday[1]), int(birthday[2]))).days + 1
    months = days / 30
    hours = days * 24
    minutes = hours * 60 
    return ("months: {}, days: {}, hours: {}, and minutes: {}".format(months, days, hours, minutes))


if __name__ == "__main__":
    age = input("How old are you? ")
    print(age_to_time(int(age)))

    birthday = input("What's your birthday? (YYYY-MM-DD) ")
    print(birthday_to_time(birthday))
