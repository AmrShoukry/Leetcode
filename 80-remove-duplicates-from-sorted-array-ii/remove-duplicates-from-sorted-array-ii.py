class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        pointer_right = length - 1
        pointer_left = 0
        current = 's'
        count = 0
        shifts = 0

        while pointer_left <= pointer_right:
            if current == nums[pointer_left]:
                if count == 1:
                    count = 2
                    pointer_left += 1
                else:
                    self.shift(nums, pointer_left, pointer_right)
                    shifts += 1
                    pointer_right -= 1
            else:
                current = nums[pointer_left]
                count = 1
                pointer_left += 1
        return length - shifts
            
    def shift(self, nums, pointer_left, pointer_right):
        while(pointer_right > pointer_left):
            nums[pointer_left] = nums[pointer_left + 1]
            pointer_left += 1
        nums[pointer_left] = '_'