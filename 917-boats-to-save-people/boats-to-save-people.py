class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people_sorted = sorted(people, reverse=True)
        boats = 0
        length = len(people)
        pointer_left = 0
        pointer_right = length - 1

        while(pointer_left <= pointer_right):
            acc = 0
            count = 0
            while (acc < limit and pointer_left <= pointer_right and count < 2):
                if people_sorted[pointer_left] + acc <= limit:
                    acc += people_sorted[pointer_left]
                    pointer_left += 1
                    count += 1
                else:
                    break

            while (acc < limit and pointer_left <= pointer_right and count < 2):
                if people_sorted[pointer_right] + acc <= limit:
                    acc += people_sorted[pointer_right]
                    pointer_right -= 1
                    count += 1
                else:
                    break
            boats += 1
            
        return boats

