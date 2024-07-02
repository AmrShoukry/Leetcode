class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for index, num in enumerate(nums):
            diff = numbers.get(target - num, 'a')
            if diff != 'a':
                return [index, diff]
            numbers[num] = index
