# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

text = input("Enter some text, and I'll output all but vowels: ")
vowels = frozenset("aeiou")
finalSet = set(text).difference(vowels)
print(sorted(finalSet))
