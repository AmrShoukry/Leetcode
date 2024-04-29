import math

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        length = len(nums)
        max_element = max(max(nums), k)
        if max_element == 0:
            return 0
        current_bit = math.floor(math.log2(max_element))
        current_value = math.pow(2, current_bit)
        current_k = k

        while(current_bit >= 0):
            accumulation = 0
            target = 0

            if current_k >= current_value:
                target = 1
                current_k -= current_value
        
            for i in range(length):
                if nums[i] >= current_value:
                    nums[i] -= current_value
                    accumulation += 1

            if accumulation % 2 != target:
                total += 1

            print(accumulation, target)

            current_bit -= 1
            current_value //= 2
        return total