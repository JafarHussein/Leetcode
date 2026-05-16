# Trying to solve the valid parenthesis problem on leetcode
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

s = "([)]"

class Solution:
    def isValid(self,s):
        list_parenthesis=list(s)
        valid_parenthesis={"(":")","[":"]","{":"}"}
        parenthesis_stack=[]
        output=True
        
        for i in range(0, len(list_parenthesis)):
            
            if valid_parenthesis.get(list_parenthesis[i]) != None:
                parenthesis_stack.append(list_parenthesis[i])
            else:
                if len(parenthesis_stack)== 0:
                    return False
                else:
                    last_item=parenthesis_stack.pop()
                    if valid_parenthesis.get(last_item) != list_parenthesis[i]:
                        return False
                    
        if len(parenthesis_stack) > 0:
            return False
            
        return output
    
    
    
sol=Solution()
print(sol.isValid(s))
                
            
