class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hashes = {}
        maximum = -9999

        for num in nums:
            value = hashes.get(num, 0)
            if value == 0:
                value = hashes.get(-num, 0)
                if value == 0:
                    hashes[num] = 1
                else:
                    hashes[num] = 2
                    absolute = abs(num)
                    if (absolute > maximum):
                        maximum = absolute
        if maximum == -9999:
            return -1
        else:
            return maximum
