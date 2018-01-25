# shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
# for item in shopping_list:
#     if item == 'spam':
#         # print("I am ignoring " + item)
#         continue
#
#     print("Buy " + item)

meal = ['egg', 'bacon', 'spam2', 'sausages']

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    nasty_food_item = ''
    print("I'll have a plate of that then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it?")

