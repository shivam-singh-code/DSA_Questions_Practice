#Question: You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
# A number which completely divides another number is called it's divisor.

# Examples:
# Input: n = 6
# Output = [1, 2, 3, 6]
# Explanation: The divisors of 6 are 1, 2, 3, 6.

# Input: n = 8
# Output: [1, 2, 4, 8]
# Explanation: The divisors of 8 are 1, 2, 4, 8.

import math

# Time complexity of O(n)
def print_all_divisor(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)


# Time Complexity
def print_all_divisor_of_n(n):
    all_divisor=[]
    sqrt_of_n = math.sqrt(n)
    # for i in range(1, int(math.sqrt(n)) + 1):
    for i in range(1, int(sqrt_of_n) + 1):
        if n % i == 0:
            all_divisor.append(i)
            if i != n/i:
                all_divisor.append(int(n/i))
    return all_divisor
    
# print_all_divisor(6)
divisor = print_all_divisor_of_n(8)
divisor.sort()
print(divisor)