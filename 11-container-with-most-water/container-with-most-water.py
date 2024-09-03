class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        pointer_left = 0
        pointer_right = length - 1
        max_area = 0

        while (pointer_right > pointer_left):
            left_height = height[pointer_left]
            right_height = height[pointer_right]
            value = (pointer_right - pointer_left) * min(left_height, right_height)
            if value > max_area:
                max_area = value
            if left_height > right_height:
                pointer_right -= 1
            else:
                pointer_left += 1
        return max_area
