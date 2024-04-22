class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_hash = {0: 1}
        result = 0
        count = 0
        for num in nums:
            result += num
            difference = result - k
            prefix_count = prefix_hash.get(difference, 0)
            count += prefix_count
            prefix_hash[result] = prefix_hash.get(result, 0) + 1
        return count