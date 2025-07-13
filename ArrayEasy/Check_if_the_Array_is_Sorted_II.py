# Check if the Array is Sorted II


# Time Complexity is O(n)
def check_if_array_is_sorted(nums):
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            else:
                return False
        return True

# print(check_if_array_is_sorted([3,4,5,1,2]))
print(check_if_array_is_sorted([1, 2, 3, 4, 5]))