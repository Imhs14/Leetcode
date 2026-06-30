# Question : 20. Valid Parentheses
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Stacks
# Difficulty : Easy

class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping of closing bracket to opening bracket
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            if char in bracket_map:  # It's a closing bracket
                # Check if stack is empty OR top doesn't match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Remove the matched opening bracket
            else:  # It's an opening bracket
                stack.append(char)
        
        # Valid only if all brackets were matched (stack is empty)
        return len(stack) == 0