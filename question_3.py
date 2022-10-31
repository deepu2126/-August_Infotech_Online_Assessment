# Write a program to find the second largest number in an array. [2.5 marks]



def sorting_function(array):
    for i in range(0, len(array)-1):
        for j in range(i, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def num_of_largest(array, index):
    return array[index-1]


array = [1, 2, 4, 6, 8, 10, 11, 7, 3]

sorted_array = sorting_function(array)

second_largest_number = num_of_largest(sorted_array[::-1], 2)
print(second_largest_number)