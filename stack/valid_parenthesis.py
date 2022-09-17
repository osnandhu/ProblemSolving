"""
PROBLEM STATEMENT:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false



"""

# solution:
class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []
        for i in s:
            print("character:",str(i))
            if i in map_dict:
                if stack and stack[-1] == map_dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if(stack):
            return False
        else:
            return True

