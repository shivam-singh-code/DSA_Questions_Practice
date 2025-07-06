# Question: You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

# Examples:
# Input: n = 25
# Output: 52
# Explanation: Reverse of 25 is 52.

# Input: n = 123
# Output: 321
# Explanation: Reverse of 123 is 321.

def reverse_number(num):
    reverse_num = 0
    while num > 0:
        last_digit = num % 10
        reverse_num = reverse_num * 10 + last_digit
        num = int(num / 10)
    return reverse_num

print(reverse_number(25))
print(reverse_number(123))
print(reverse_number(1980))