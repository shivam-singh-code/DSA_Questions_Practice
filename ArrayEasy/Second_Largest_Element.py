# Find Second Smallest and Second Largest Element in an array

# Best solution with time complexity of O(n)
def second_largest(my_list):
    largest = -1
    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
    
    second_largest  = -1
    for i in range(len(my_list)):
        if my_list[i] > second_largest and my_list[i] != largest:
            second_largest = my_list[i]
    
    return second_largest

# print(second_largest([1,2,4,7,7,5]))



# Time complexity is o(n) but optimal due to single loop
def second_largest_optimal(my_list):
    largest = my_list[0]
    second_largest = -1

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        
        if my_list[i] < largest and my_list[i] > second_largest:
            second_largest = my_list[i]
    
    return second_largest

# print(second_largest_optimal([1,2,4,7,7,5]))

def second_smallest_element(my_list):
    # asssuming the array does not contain negative element
    smallest = my_list[0]
    # either take first element or any big number possible
    second_smallest = 10000
    
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]
        
        if my_list[i] != smallest and my_list[i] < second_smallest:
            second_smallest = my_list[i]

    return second_smallest

# print(second_smallest_element([1,2,4,7,7,5]))
print(second_smallest_element([1,2,4,7,7,5,-1, -2]))

