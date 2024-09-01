class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        rotations = k % length

        self.reverse_array(nums, 0, length - 1)
        self.reverse_array(nums, 0, rotations - 1)
        self.reverse_array(nums, rotations, length - 1)

    def reverse_array(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1