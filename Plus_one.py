"""
Plus One Problem
================

Problem Description:
--------------------
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeros.

Your task is to increment the large integer by one and return the resulting array of digits.

Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]

Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]

Example 3:
    Input: digits = [9]
    Output: [1,0]
"""

def plus_one(digit):
    """
    Solution 1: Convert the list of digits into an integer, increment it, and convert it back to a list.
    
    Steps:
    1. Convert each digit to a string and join them to form a number.
    2. Convert this string to an integer and add 1.
    3. Convert the incremented number back to a list of digits.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    num = int("".join(map(str, digit)))  # Convert list to integer
    num += 1  # Increment by 1
    return [int(i) for i in str(num)]  # Convert back to list


def plus_one_2(digit):
    """
    Solution 2: Process the list in reverse, handling carry manually.
    
    Steps:
    1. Start from the last digit and check if it is less than 9.
    2. If it is, increment it and return immediately.
    3. If it is 9, set it to 0 and move to the previous digit.
    4. If all digits were 9, prepend 1 to the list.
    
    Time Complexity: O(n)
    Space Complexity: O(1) (modifies input list directly)
    """
    n = len(digit)
    
    for i in range(n - 1, -1, -1):  # Traverse from last digit to first
        if digit[i] < 9:
            digit[i] += 1  # Increment and return if not 9
            return digit
        digit[i] = 0  # If 9, set to 0 and continue
    
    return [1] + digit  # If all were 9, add a new leading 1


# Example test cases
digits = [1, 2, 3]
print(plus_one(digits))   # Output: [1, 2, 4]
print(plus_one_2(digits)) # Output: [1, 2, 4]

digits = [9, 9, 9]
print(plus_one(digits))   # Output: [1, 0, 0, 0]
print(plus_one_2(digits)) # Output: [1, 0, 0, 0]
