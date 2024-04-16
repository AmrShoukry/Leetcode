class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for index, num in enumerate(nums):
            numbers[num] = numbers.get(num, index)

        for index, num in enumerate(nums):
            difference = target - num
            value = numbers.get(difference, 'a')
            if value != 'a' and value != index:
                return [index, value]
                
