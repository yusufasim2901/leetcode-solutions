class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
            
        for i in range(len(coordinates) - 1, 1, -1):
            p3 = coordinates[i]
            p2 = coordinates[i-1]
            p1 = coordinates[i-2]
            
            dy_son = p3[1] - p2[1]
            dx_son = p3[0] - p2[0]
            dy_onceki = p2[1] - p1[1]
            dx_onceki = p2[0] - p1[0]
            
            if dy_son * dx_onceki != dy_onceki * dx_son:
                return False
                
        return True