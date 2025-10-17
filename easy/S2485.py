class Solution(object):
    def pivotInteger(self, n):
        x = math.sqrt((n * (n + 1))/2)
        if x == int(x):
         return int(x)
        else:
         return -1