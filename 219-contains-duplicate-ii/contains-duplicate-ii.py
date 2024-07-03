class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashNums = {}
        for index, num in enumerate(nums):
            idx = hashNums.get(num, -1)
            if idx != -1:
                if index - idx <= k:
                    return True
                else:
                    hashNums[num] = index
            else:
                hashNums[num] = index
        return False