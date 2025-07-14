# Intersection of two sorted array


def find_intersection_of_sorted_arrays(num1, num2):
    intersec_arr = []
    i = 0
    j = 0
    
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            i += 1
        elif num2[j] < num1[i]:
            j+= 1
        else:
            intersec_arr.append(num1[i])
            i += 1
            j += 1
    
    return intersec_arr

print(find_intersection_of_sorted_arrays([1, 2, 3, 4, 5], [1, 2, 7]))
print(find_intersection_of_sorted_arrays([3, 4, 6, 7, 9, 9], [1, 5, 7, 8, 8]))