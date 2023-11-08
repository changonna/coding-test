'''
stack이 비어있지 않고 마지막값이 p와 같으면 pop하고
전체 문자를 다 돌고나서 비어있으면 True를 반환
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "{":
                stack.append("}")
            elif p == "[":
                stack.append("]")
            elif p == "(":
                stack.append(")")
            elif stack and stack[-1] == p:
                stack.pop()
            else:
                return False

        return not stack
           

s = "[({})]"
s = "[)]"
solution = Solution()
boo = solution.isValid(s)
print(boo)