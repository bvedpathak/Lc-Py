'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution(object):
    def isValid(self, s):
        if not s:
            return False
        
        lookup = { ')' : '(', '}' : '{', ']' : '[' }
        stack = list()

        for token in s:
            if token == ')' or token == '}' or token == ']':
                if not stack or stack[-1] != lookup.get(token):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(token)
        return len(stack) == 0
s  = ""    
#s = "([])"
#s = "()[]{}"
#s = "(]"


print(f"\nIs {s} is valid: {Solution().isValid(s)}\n")
