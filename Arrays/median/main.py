# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combined_array = nums1 + nums2
        combined_array.sort()
        
        first_index = len(combined_array) // 2
        
        if len(combined_array) % 2 == 0:
            second_index = first_index - 1
            median = (combined_array[first_index] + combined_array[second_index]) / 2.0
            return median
        else:
            median = float(combined_array[first_index])
            return median

nums1 = [1, 2]
nums2 = [3, 4]     
sol_instance = Solution()
print(sol_instance.findMedianSortedArrays(nums1, nums2)) 
            