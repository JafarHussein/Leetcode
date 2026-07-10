class Solution:
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        
        while left < right:
            current_sum=numbers[left] + numbers[right]
            
            if current_sum == target:
                left+=1
                right+=1
                
                return [left, right]
            
            elif current_sum < target:
                left+=1
                
            else:
                right-=1
                
        return None
                
numbers=[2,7,11,15]
              
sol_instance=Solution()
print(sol_instance.twoSum(numbers, target=9))
                
            