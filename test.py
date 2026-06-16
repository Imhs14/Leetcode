# Test your code Pieces
class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in char_map: # check if the char in char map or not
                # 1st check if stack is not empty,  2nd check if last stack char is not equal to current char
                if not stack or stack[-1] != char_map[char]: 
                    # if its not equal return False reason may be stack is empty or 
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0 # if this is true we return true that means we have successfully popped every element 
                                # elese false will be returned as there was mis match of the closing brackets or stack was empty