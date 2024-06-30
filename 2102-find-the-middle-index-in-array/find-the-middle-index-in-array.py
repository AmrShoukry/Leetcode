class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        left = 0
        
        for index, num in enumerate(nums):
            right = total - num
            if left == right:
                return index
            left += num
            total -= num
        
        return -1