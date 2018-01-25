# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment
#
segments = 1
length = 0
IP = input("Enter an IP address: ")
# char = ""
if IP[-1] != ".":
    IP += "."
for char in IP:
    if char == ".":
        print("Segment {} has length of {}".format(segments, length))
        segments += 1
        length = 0
    else:
        length += 1
# if char != ".":
#     print("Segment {} has length of {}".format(segments, length))
