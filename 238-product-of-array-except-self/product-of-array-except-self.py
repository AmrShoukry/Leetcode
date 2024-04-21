class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix = [1] * (nums_len + 1)
        suffix = [1] * (nums_len + 1)
        output = [1] * nums_len
        suffix_pointer = nums_len - 1

        product_prefix = 1
        product_suffix = 1
        prefix[0] = product_prefix
        suffix[nums_len] = product_suffix
        for i in range(nums_len):
            product_prefix *= nums[i]
            prefix[i + 1] = product_prefix
            product_suffix *= nums[suffix_pointer]
            suffix[suffix_pointer] = product_suffix
            suffix_pointer -= 1

        for i in range(nums_len):
            output[i] = prefix[i] * suffix[i + 1]
        return output
