#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given non-negative integer using recursion.

# Parameters:
# - n: An integer representing the number whose factorial is to be calculated.

# Returns:
# Returns the factorial of the input integer n.
def factorial(n):
    # Base case: if n is 0, return 1 as the factorial of 0 is defined as 1.
    if n == 0:
        return 1
    # Recursive case: if n is not 0, calculate factorial by recursively calling the function
    # with n-1 and multiplying the result with n.
    else:
        return n * factorial(n-1)

# Retrieve the input argument from the command line and convert it to an integer.
# Calculate the factorial of the input integer using the factorial function.
f = factorial(int(sys.argv[1]))

# Print the calculated factorial.
print(f)
