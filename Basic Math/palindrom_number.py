# Question: You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.

# A palindrome number is a number which reads the same both left to right and right to left.


# Examples:
# Input: n = 121
# Output: true
# Explanation: When read from left to right : 121.
# When read from right to left : 121.

# Input: n = 123
# Output: false
# Explanation: When read from left to right : 123.
# When read from right to left : 321.

def is_plaindrom(num):
    num_copy = num
    reverse_number = 0
    while num > 0:
        last_digit = num % 10
        reverse_number = reverse_number * 10 + last_digit
        num = int(num / 10)
    # print(reverse_number)
    return num_copy == reverse_number

print("isPlaindrom: ",is_plaindrom(121))
print("isPlaindrom: ",is_plaindrom(123))
print("isPlaindrom: ",is_plaindrom(1032))