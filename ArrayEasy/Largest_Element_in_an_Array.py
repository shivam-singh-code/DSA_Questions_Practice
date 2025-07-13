# Find the Largest element in an array

def larget_element(my_list):
    largest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[0] < my_list[i]:
            largest = my_list[i]
    return largest

# print(larget_element([1,2,3,4,5]))
print(larget_element([3,2,1,5,2]))