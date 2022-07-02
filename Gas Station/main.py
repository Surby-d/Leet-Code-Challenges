class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        
        start, tank = 0, 0
        for x in range(len(gas)):
            tank += gas[x]-cost[x]
            if tank<0:
                start = x+1
                tank = 0
            
        return start
            
