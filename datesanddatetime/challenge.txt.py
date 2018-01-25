# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import pytz
import datetime
x = 'PH'
# print("\t\t{}".format(pytz.country_names[x]), end=': ')
choices = {}
zones=[]
if x in pytz.country_timezones:
    for zone in sorted(pytz.country_timezones[x])[:9]:
        # tz_to_display = pytz.timezone(zone)
        # local_time = datetime.datetime.now(tz=tz_to_display)
        zones.append(zone)
else:
    print("\t\tNo timezone defined")
for i, item in enumerate(zones, start=1):
    choices[str(i)] = item
    print("\t\t({}) {}".format(i, item))
print("\t\t(0) Quit (I do not want to pick)")
choice = 0
while True:
    choice = input()
    if choice == '0':
        break

    if choice in choices.keys():
        tz_to_display = pytz.timezone(choices[choice])
        choice_time = datetime.datetime.now(tz=tz_to_display)
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        print("The time in {} is {} {}".format(choices[choice], choice_time.strftime('%A %x %X %z'), choice_time.tzname()))
        print("Local time is {}".format(local_time.strftime('%A %x %X %z')))
        print("UTC time is {}".format(utc_time.strftime('%A %x %X %z')))





