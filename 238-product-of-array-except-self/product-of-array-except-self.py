class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        output = [1] * nums_len
        suffix_pointer = nums_len - 1

        product_prefix = 1
        product_suffix = 1
        for i in range(nums_len - 1):
            product_prefix *= nums[i]
            product_suffix *= nums[suffix_pointer]
            output[i + 1] *= product_prefix
            output[suffix_pointer - 1] *= product_suffix
            suffix_pointer -= 1

        return output
