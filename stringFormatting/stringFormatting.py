age = 24
print("My age is " + str(age) + "years")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31, "January", "March", "May", "July",
                                                                       "August", "October", "December"))
print("""\
January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September:{1}
October: {2}
November: {1}
December: {2}\
""".format(28, 30, 31))
# deprecated but used often in python2
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %3d and cubed is %4d" %(i, i ** 2, i ** 3))

print("Pi is approxiamately %12.50f" % ( 22 / 7))
import math
#new in python3
for i in range(1, 13):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4} and pi is {3:12.5}".format(i, i ** 2, i ** 3, 22 / 7))

for i in range(1, 13):
    print("No. {:2} squared is {:4} and cubed is {:4} and pi is {:<12.5}".format(i, i ** 2, i ** 3, 22 / 7))