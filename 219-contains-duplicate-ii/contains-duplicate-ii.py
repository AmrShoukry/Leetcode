class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pointer = 0
        length = len(nums)
        hashes = {}

        while pointer < length:
            if abs(hashes.get(nums[pointer], 99999) - pointer) <= k:
                return True
            hashes[nums[pointer]] = pointer
            pointer += 1

        return False