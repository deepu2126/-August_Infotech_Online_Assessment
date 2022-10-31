

def Bubble_sort(array):
    for i in range(0, len(array)-1):
        for j in range(i, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


array = [1, 2, 4, 6, 8, 10, 11, 7, 3]

print(Bubble_sort(array))