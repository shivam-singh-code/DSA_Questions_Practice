# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

# Examples:
# Input: n = 153
# Output: true
# Explanation: Number of digits : 3.
# 13 + 53 + 33 = 1 + 125 + 27 = 153.
# Therefore, it is an Armstrong number.

# Input: n = 12
# Output: false
# Explanation: Number of digits : 2.
# 12 + 22 = 1 + 4 = 5.
# Therefore, it is not an Armstrong number.


def is_armstrong_number(num):
    num_copy = num
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += last_digit ** 3
        num = int(num/10)
    return num_copy == sum

print(is_armstrong_number(153))
print(is_armstrong_number(12))
# print(is_armstrong_number())