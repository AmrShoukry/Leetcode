class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        newArr = [-1] * (length + 1)
        for num in nums:
            newArr[num] = 1
        for index, num in enumerate(newArr):
            if num == -1:
                return index