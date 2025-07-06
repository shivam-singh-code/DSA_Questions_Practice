import math
# # Question 
# You are given an integer n. You need to return the number of digits in the number.

# The number will have no leading zeroes, except when the number is 0 itself.

# Examples:
# Input: n = 4
# Output: 1
# Explanation: There is only 1 digit in 4.

# Input: n = 14
# Output: 2
# Explanation: There are 2 digits in 14.

def count(n):
    temp_count = 0
    while(n > 0):
        temp_count += 1
        n = int(n/10)
    return temp_count


def count_with_logrithm(n):
    digit_count = int(math.log10(n)) + 1
    return digit_count
        
print(count(498))
print(count_with_logrithm(7789))

# Time Complexity is O(log10(N)) since the divison in done with 10 if it was 2 then log2 if it was 5 then log5