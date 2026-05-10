class Solution:
    def romanToInt(self, s):
        roman_values={"M":1000,
              "D":500,
              "C":100,
              "L":50,
              "X":10,
              "V":5,
              "I":1}
        individual_letter_list=list(s)
        empty_list=[]
        sum=0
        for i in range(0, len(individual_letter_list)):
            for j in range(i+1, len(individual_letter_list)):
                current_value=roman_values.get(individual_letter_list[i])
                next_value=roman_values.get(individual_letter_list[j])
                if current_value > next_value:
                    empty_list.append(current_value)
                else:
                    empty_list.append(next_value-current_value)
                break
            
        for value in empty_list:
            sum+=value
            
        return sum
        

sol=Solution()
print(sol.romanToInt("MCMXCIV"))
            
        
        