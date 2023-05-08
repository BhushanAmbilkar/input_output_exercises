# Exercise 6: Write all content of a given file into a new file by skipping line number 5


# Create a test.txt file and add the below content to it.
#
# Given test.txt file:
#
# line1
# line2
# line3
# line4
# line5
# line6
# line7

# Show Hint
# Read all lines from a test.txt file using the readlines() method. This method returns all lines from a file as a list
# Open new text file in write mode (w)
# Set counter = 0
# Iterate each line from a list
# if the counter is 4, skip that line, else write that line in a new text file using the write() method
# Increment counter by 1 in each iteration

# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1


