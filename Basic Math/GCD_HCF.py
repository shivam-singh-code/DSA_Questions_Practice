#Question: You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
# The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.




# Examples:
# Input: n1 = 4, n2 = 6
# Output: 2
# Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6


# Greatest Common divisor = 2.
# Input: n1 = 9, n2 = 8
# Output: 1
# Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.
# Greatest Common divisor = 1.




# Time complexity is O(n)
def find_GCD(n1,n2):
    gcd = 0
    for i in range(1, min(n1,n2)+1, 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd


# Eculiden algorithm gcd(n1,n2) = gcd(n1-n2) where n1>n2
# we will do is n1%n2 if n1>n2 else n2%n1 untill one number is zero and remaning number will be GCD
def find_GCD_eculiden_alog(n1,n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
   
    if n1 == 0:
        return n2
    return n1


# print(find_GCD(4,6))
# print(find_GCD(9,8))


print(find_GCD_eculiden_alog(4,6))
print(find_GCD_eculiden_alog(9,8))