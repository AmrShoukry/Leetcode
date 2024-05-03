class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        pointer1 = 0 
        pointer2 = 0
        length1 = len(version1)
        length2 = len(version2)
        while (pointer1 < length1 or pointer2 < length2):
            sum1 = 0
            sum2 = 0

            while (pointer1 < length1 and version1[pointer1] != '.'):
                sum1 = sum1 * 10 + int(version1[pointer1])
                pointer1 += 1
            
            while(pointer2 < length2 and version2[pointer2] != '.'):
                sum2 = sum2 * 10 + int(version2[pointer2])
                pointer2 += 1

            if sum1 < sum2:
                return -1
            elif sum1 > sum2:
                return 1

            pointer1 += 1
            pointer2 += 1
        return 0
        