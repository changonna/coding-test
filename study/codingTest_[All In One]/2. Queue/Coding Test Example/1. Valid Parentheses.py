'''
pairs(짝)를 활용
'''

class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            elif stack and c == pairs[stack.pop()]: # stack이 비어있지 않고 + pop한 값의 짝과 c가 같으면
                pass
            else:
                return False
        return not stack

valid = Solution()
s = "[({})]"
boo = valid.isValid(s)
print(boo)