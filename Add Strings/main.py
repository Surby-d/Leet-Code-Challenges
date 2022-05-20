class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = {str(i):i for i in range(10)}
        d['carry'] = 0
        result = []
        num1, num2 = list(num1), list(num2)
        while len(num1)!=len(num2):
            if len(num1)<len(num2):
                num1.insert(0, '0')
            elif len(num1)>len(num2):
                num2.insert(0, '0')
                
        for i in range(len(num1)-1, -1, -1):
            val = str(d[num1[i]]+d[num2[i]]+d['carry'])
            if i==0:
                result.insert(0, val)
                continue
            result.insert(0, val[-1])
            if len(val)>1:
                d['carry'] = int(val[0])
            else:
                d['carry'] = 0
                
                
        return ''.join(result)
