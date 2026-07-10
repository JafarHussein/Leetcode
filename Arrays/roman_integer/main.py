class Solution:
    def romanToInt(self,s):
        individual_letter_list=list(s)
        roman_values=roman_values={"M":1000,
              "D":500,
              "C":100,
              "L":50,
              "X":10,
              "V":5,
              "I":1}
        skip_next=False
        sum=0
        empty_list=[]
        
        for i in range(0, len(individual_letter_list)):
            if skip_next:
                skip_next=False
                continue
            found_subtraction=False
            for j in range(i+1, len(individual_letter_list)):
                current_value=roman_values.get(individual_letter_list[i])
                next_value=roman_values.get(individual_letter_list[j])
               
                if next_value > current_value:
                    empty_list.append(next_value-current_value)
                    skip_next=True
                    found_subtraction=True
                break
                    
            if not found_subtraction:
                    empty_list.append(roman_values.get(individual_letter_list[i]))
                    
        for value in empty_list:
            sum+=value
            
        return sum
           
    
sol=Solution()
print(sol.romanToInt("MCMXCIV"))
            
            
        
                    
                
                   
                    
            
        
        