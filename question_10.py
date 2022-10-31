# Write a program or algorithm for Two Elements whose sum is closest to zero. [2.5 marks]

# Example

# You are given an array [-23, 12, -35, 45, 20, 36] then the two elements would be -35 & 36 as their pair sum is 1 which is closest to 0


array = [-23, 12, -35, 45, 20, 36] 

left = []
right = []

for i in range(0, len(array)):
    for j in range(i, len(array)):
        if i != j:
            if array[i] + array[j] < 0:
                left.append(array[i] + array[j])
            else:
                right.append(array[i] + array[j])

left_res, right_res = sorted(left)[::-1], sorted(right)

if (left_res[0] * -1) > right_res[0]:
    result = right_res[0]
else:
    result = left_res[0]

print(result)