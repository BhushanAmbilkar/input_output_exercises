# Exercise 10: Read line number 4 from the following file

# Create a test.txt file and add the below content to it.

# test.txt file:

# line1
# line2
# line3
# line4
# line5
# line6
# line7

# read file
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])
