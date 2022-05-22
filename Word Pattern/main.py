class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = dict()
        l = s.split(' ')
        if len(pattern)!=len(l): return False
        if len(set(pattern))!=len(set(l)): return False
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]] = pattern[i]
            elif d[l[i]] != pattern[i]:
                return False
            
        return True
