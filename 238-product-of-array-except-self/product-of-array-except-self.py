class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix = [1] * (nums_len + 1)
        suffix = [1] * (nums_len + 1)
        output = [1] * nums_len

        product = 1
        prefix[0] = product
        for i in range(nums_len):
            product *= nums[i]
            prefix[i + 1] = product

        product = 1
        suffix[nums_len] = product
        for i in range(nums_len - 1, -1, -1):
            product *= nums[i]
            suffix[i] = product

        for i in range(nums_len):
            output[i] = prefix[i] * suffix[i + 1]
        return output
