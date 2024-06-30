class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length1 = len(nums1)
        length2 = len(nums2)
        indicies = {}
        greaters = [-1] * length1 
        for i in range(length2 - 1, -1 ,-1):
            if i + 1 < length2:
                created = nums2[i + 1]
                while created < nums2[i]:
                    created = indicies[created]
                    if created == -1:
                        break
                
                indicies[nums2[i]] = created
            else:
                indicies[nums2[i]] = -1
        
        for index, num in enumerate(nums1):
            greaters[index] = indicies[num]

        print(indicies)
        return greaters
