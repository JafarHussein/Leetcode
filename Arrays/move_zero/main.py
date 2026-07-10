# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
nums = [0,1,0,3,12]

class Solution(object):
   def moveZeroes(self, nums):
       left=0
       
       for counter in range(0, len(nums)):
           if nums[counter] != 0:
               nums[left], nums[counter] = nums[counter], nums[left]
               left+=1
               
sol_instance=Solution()
print(sol_instance.moveZeroes(nums))