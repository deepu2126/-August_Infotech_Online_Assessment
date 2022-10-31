# Given an integer array numbers and return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. [5 marks]

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]


nums = [-1,0,1,2,-1,-4]
all_possible_triples = []
for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        for k in range(0, len(nums)):
            if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k] and sum([nums[i], nums[j], nums[k]]) == 0:
                pass
                # print(nums[i], nums[j], nums[k])


tripletList = []

for x in range(len(nums)-2): 
    for y in range(x+1,len(nums)-1):
        for z in range(y+1,len(nums)):
            print(x, y, z)
            if nums[x]+nums[y]+nums[z]==0:
                tempList = []
                tempList.extend([nums[x],nums[y],nums[z]])
                tempList.sort()
                if tempList not in tripletList:
                    tripletList.append(tempList)
                    tempList=[]
                    ExistFlag=True

print(tripletList)
