class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pointer1 = 0
        pointer2 = 0
        length = len(nums)
        hashes = {}

        while pointer2 < length:
            if pointer2 - pointer1 <= k:
                val = hashes.get(nums[pointer2], 0)
                if val == 0:
                    hashes[nums[pointer2]] = 1
                else:
                    return True
                pointer2 += 1
            else:
                hashes[nums[pointer1]] = 0
                val = hashes.get(nums[pointer2], 0)
                if val == 0:
                    hashes[nums[pointer2]] = 1
                else:
                    return True
                pointer1 += 1
                pointer2 += 1
        return False