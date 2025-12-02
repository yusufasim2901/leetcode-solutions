class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            
            if x != y:
                stones.append(y - x)
        
        return stones[0] if stones else 0