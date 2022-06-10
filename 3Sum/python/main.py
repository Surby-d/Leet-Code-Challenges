class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        pos, neg, zer = [], [], []
        for i in nums:
            if i<0: neg.append(i)
            elif i>0: pos.append(i)
            else: zer.append(i)
                
        positive, negative = set(pos), set(neg)
        if zer:
            for p in positive:
                if -p in negative:
                    result.add((-p, 0, p))
                    
        if len(zer)>=3:
            result.add((0, 0, 0))
            
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                val = -(pos[i]+pos[j])
                if val in negative:
                    result.add(tuple(sorted([val, pos[i], pos[j]])))
                    
                    
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                val = -(neg[i]+neg[j])
                if val in positive:
                    result.add(tuple(sorted([neg[i], neg[j], val])))
                    
        return result
        
                
                        
