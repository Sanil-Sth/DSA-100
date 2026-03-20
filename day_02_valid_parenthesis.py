"""
Day 02 — Valid Parentheses
==========================
LeetCode #20 | Difficulty: Easy | Topic: Stack

Problem:
    Given a string s of bracket characters '()[]{}'.
    Return True if every bracket is properly opened and closed in order.

Pattern: Stack — Last In, First Out matching
    Push openers; on a closer, check and pop the top of the stack.

Approach:
    - Use a dict to map each closer to its expected opener.
    - Iterate through the string:
        - Opening bracket → push to stack
        - Closing bracket → check stack top matches, else return False
    - At the end, stack must be empty.

Time Complexity:  O(n)
Space Complexity: O(n)

Examples:
    isValid("()[]{}") → True
    isValid("([)]")   → False
    isValid("{[]}")   → True
"""

def isValid(s: str) -> bool:
    if len(s) % 2 != 0:   # odd length can never be valid
        return False
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack
# Test cases
print(isValid("()[]{}"))  # True
print(isValid("([)]"))    # False
print(isValid("{[]}"))    # True
