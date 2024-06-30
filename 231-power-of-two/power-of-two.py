import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        result = math.log2(n)
        return result - int(result) == 0
