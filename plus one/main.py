class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]==9:
            s = [str(i) for i in digits]
            digit = list(str(int(''.join(s)) + 1))
            return digit
            
        
        digits[-1] = digits[-1]+1
        return digits
                
        
            
