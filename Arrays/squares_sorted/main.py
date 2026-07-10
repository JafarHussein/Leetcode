# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution(object):
    def sortedSquares(self, nums):
        #lets start by squaring all the values in the array num
        squares=[]
        sorted_squares=[]
        for number in nums:
            squares.append(number * number)
            
        left=0
        right=len(squares)-1
        
        while left <= right:
            if squares[left] > squares[right]:
                sorted_squares.append(squares[left])
                left+=1
                
            elif squares[right] > squares[left]:
                sorted_squares.append(squares[right])
                right-=1
                
            elif squares[left] == squares[right]:
                sorted_squares.append(squares[left])
                left+=1
                
                
                
        return sorted_squares[::-1]
                
        
        
    
nums = [-7,-3,2,3,11]
sol_instance=Solution()
print(sol_instance.sortedSquares(nums))
