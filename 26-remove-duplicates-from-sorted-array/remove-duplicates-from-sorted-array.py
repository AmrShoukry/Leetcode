class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total = 0
        length = len(nums)
        pointer_ = length - 1
        pointerMove = length - 1
        current = 's'

        while (pointerMove >= 0):
            if(nums[pointerMove] == current):
                current = 's'
                for i in range(pointerMove + 1, pointer_ + 1):
                    nums[i - 1] = nums[i]
                nums[pointer_] = '_'
                pointer_ -= 1
                total += 1
            else:
                current = nums[pointerMove]
                pointerMove -= 1

        return length - total