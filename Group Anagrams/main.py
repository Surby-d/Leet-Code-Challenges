class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {''.join(sorted(i)):[] for i in strs}
        dkeys = list(d.keys())
        for word in strs:
            d[''.join(sorted(word))].append(word)
            
        anagrams = []
        for key in dkeys:
            anagrams.append(d[key])
            
        return anagrams
        
            
        
