# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.



# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.


# Examples:
# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

# Output: [1, 2, 3, 4, 5, 7]

# Explanation: The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2


def find_union_of_sorted_array(num1, num2):
    union_arr = []
    num1_pointer = 0
    num2_pointer = 0

    while num1_pointer < len(num1) and num2_pointer < len(num2):
        if num1[num1_pointer] < num2[num2_pointer]:
            if len(union_arr) == 0 or union_arr[len(union_arr)-1] != num1[num1_pointer]:
                union_arr.append(num1[num1_pointer])
            num1_pointer += 1
        else:
            if len(union_arr) == 0 or union_arr[len(union_arr)-1] != num2[num2_pointer]:
                union_arr.append(num2[num2_pointer])
            num2_pointer += 1

    while num2_pointer < len(num2):
        if len(union_arr) == 0 or union_arr[len(union_arr)-1] != num2[num2_pointer]:
            union_arr.append(num2[num2_pointer])
        num2_pointer += 1

    while num1_pointer < len(num1):
        if len(union_arr) == 0 or union_arr[len(union_arr)-1] != num1[num1_pointer]:
            union_arr.append(num1[num1_pointer])
        num1_pointer += 1

    return union_arr

# print(find_union_of_sorted_array([1, 2, 3, 4, 5], [1, 2, 7]))
print(find_union_of_sorted_array([3, 4, 6, 7, 9, 9], [1, 5, 7, 8, 8]))