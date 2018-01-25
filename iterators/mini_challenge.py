# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function
#
# Use a for lop to loop "n" times, where n is the number of items in your list.
# each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

items = list(range(15))
iter_1 = iter(items)
for i in range(len(items)):
    print(next(iter_1))
