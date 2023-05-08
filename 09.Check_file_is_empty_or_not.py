# Exercise 9: Check file is empty or not
# Write a program to check if the given file is empty or not

# Show Hint
# Use os.stat('file_name').st_size() function to get the file size. if it is 0 then the file is empty.

import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')
