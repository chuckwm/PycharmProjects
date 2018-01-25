list_1 = []
list_2 = list()

# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal".split(" ")))
#
# even = [2, 4, 6, 8]
#
# another_even = even
#
# print(another_even is even)
#
# another_even = list(even)
#
# print(another_even is even)
# print(another_even == even)
#
# another_even.sort(reverse=True)
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
# print(numbers)

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)