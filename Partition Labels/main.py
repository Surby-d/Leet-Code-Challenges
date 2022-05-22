class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions, n, i, maxlen = [], len(s), 0, 0
        while sum(partitions)<n:
            s = s[maxlen:]
            i, maxlen = 0, 0
            while i<=maxlen:
                l, r = i, s.rindex(s[i])
                maxlen = max(r, maxlen)
                i+=1
            maxlen+=1
            partitions.append(maxlen)

        return partitions
