class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedResult = (n * (n + 1)) // 2
        result = 0
        for num in nums:
            result += num
        return expectedResult - result