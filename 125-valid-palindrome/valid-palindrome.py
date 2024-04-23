class Solution:
    def isPalindrome(self, s: str) -> bool:

        length = len(s)

        end_pointer = length - 1
        start_pointer = 0

        while(start_pointer < end_pointer):
            start = s[start_pointer]
            end = s[end_pointer]

            if not (start.isalpha() or start.isdigit()):
                start_pointer +=1 
                continue

            if not (end.isalpha() or end.isdigit()):
                end_pointer -=1 
                continue

            if (start.lower() != end.lower()):
                return False

            start_pointer += 1
            end_pointer -= 1
        
        return True