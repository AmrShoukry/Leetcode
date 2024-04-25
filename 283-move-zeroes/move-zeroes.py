class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer_0 = 0
        pointer_n = 0
        length = len(nums)

        while(pointer_n < length):
            if nums[pointer_0] == 0 and nums[pointer_n] != 0:
                self.swap(nums, pointer_0, pointer_n)
                pointer_0 += 1
            elif nums[pointer_0] != 0:
                pointer_0 += 1
            pointer_n += 1

    def swap(self, nums, pointer_0, pointer_n):
        temp = nums[pointer_0]
        nums[pointer_0] = nums[pointer_n]
        nums[pointer_n] = temp