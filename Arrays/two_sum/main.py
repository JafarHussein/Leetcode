# Trying to solve a two sum question in py

nums=[2,7,11,15]

class Solution:
    def two_sum(nums, target):
        solution_list=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    solution_list.append(i)
                    solution_list.append(j)
        return solution_list
    

print(Solution.two_sum(nums, 9))

# The solution to this problem

#1. You initialize an empty list inside the function
#2. You declare two nested loops that one starting from 0 and the other starting from 1, you loop through the numbers adding the nums and the index of i and j , if they equal the target you return the indexes, other wise you return an empty list
    
