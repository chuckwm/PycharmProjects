# Ask person for their name and their age, then check if the person is eligible for
# going on an 18-30 holiday.
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
if 17 < age < 31:
    print("Welcome to the holiday {}!".format(name))
else:
    print("\
We're sorry {}, this party is only for folks between the ages of 18 \
and 30.".format(name))
