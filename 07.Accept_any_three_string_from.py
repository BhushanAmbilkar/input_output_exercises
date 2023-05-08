# Exercise 7: Accept any three string from one input() call

# Write a program to take three names as input from a user in the single input() function call.

# Show Hint
# Ask the user to enter three names separated by space
# Split input string on whitespace using the split() function to get three individual names

str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)

