class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left_pointer = 0
        right_pointer = length - 1

        while (right_pointer > left_pointer):
            if numbers[right_pointer] + numbers[left_pointer] == target:
                return [left_pointer + 1, right_pointer + 1]
            elif numbers[right_pointer] + numbers[left_pointer] > target:
                right_pointer -= 1
            elif numbers[right_pointer] + numbers[left_pointer] < target:
                left_pointer += 1
