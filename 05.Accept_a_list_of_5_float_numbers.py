# Exercise 5: Accept a list of 5 float numbers as an input from the user

# Show Hint
# Create a list variable named numbers
# Run loop five times
# In each iteration of the loop, use the input() function to take input from a user
# Convert user input to float number using the float() constructor
# Add float number to the numbers list using the append() function

numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)