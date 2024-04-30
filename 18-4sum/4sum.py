class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() 
        output = []
        length = len(nums)
        pointer_0 = 0

        while pointer_0 < length - 3: 
            pointer_1 = pointer_0 + 1
            
            while pointer_1 < length - 2:  
                pointer_2 = pointer_1 + 1
                pointer_3 = length - 1

                while pointer_2 < pointer_3:
                    current_sum = nums[pointer_0] + nums[pointer_1] + nums[pointer_2] + nums[pointer_3]

                    if current_sum == target:
                        output.append([nums[pointer_0], nums[pointer_1], nums[pointer_2], nums[pointer_3]])
                        
                        while pointer_2 < pointer_3 and nums[pointer_2] == nums[pointer_2 + 1]:
                            pointer_2 += 1
                        pointer_2 += 1
                        
                        while pointer_2 < pointer_3 and nums[pointer_3] == nums[pointer_3 - 1]:
                            pointer_3 -= 1
                        pointer_3 -= 1

                    elif current_sum < target:
                        pointer_2 += 1
                    else:
                        pointer_3 -= 1
                
                while pointer_1 < length - 2 and nums[pointer_1] == nums[pointer_1 + 1]:
                    pointer_1 += 1
                pointer_1 += 1
                
            while pointer_0 < length - 3 and nums[pointer_0] == nums[pointer_0 + 1]:
                pointer_0 += 1
            pointer_0 += 1

        return output
