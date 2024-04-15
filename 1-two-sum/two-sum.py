class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maximum = len(nums)
        for index, num in enumerate(nums):
            for i in range(index + 1, maximum):
                if num + nums[i] == target:
                    return [index, i]