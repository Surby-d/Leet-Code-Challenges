class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1, 1]
        else:
            val = [1, 1]
            for i in range(1, rowIndex):
                temp = [1, 1]
                ind = 1
                while ind<i+1:
                    temp.insert(ind, val[ind-1]+val[ind])
                    ind+=1

                val = temp


        return val
