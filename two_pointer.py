nums=[1, 3, 5, 8, 12]

def targetSum(nums, target):
    right=0
    left=len(nums)-1
    
    while right < left:
        current_sum=nums[right] + nums[left]
        
        if current_sum == target:
            return [right, left]
        
        elif current_sum < target:
            right+=1
            
        else:
            right-=1
            
    return None


print(targetSum(nums, 22))