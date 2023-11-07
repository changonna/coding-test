'''
stack을 생성하고
({[ 대신 
]}) 를 append해서
pop할때 값을 비교해서 판단한다
'''

class Solution(object):
    def isValid(self, s):
        stack = []

        for p in s:
            if p == "(":
                stack.append(")")
            elif p == "{":
                stack.append("}")
            elif p == "[":
                stack.append("]")
            # ")}]"가 들어올때
            # stack이 비어있거나 / pop() 값이 그 문자와 같지 않으면
            elif not stack or stack.pop() != p:
                return False
        return not stack
           

s = "[({})]"
solution = Solution()
boo = solution.isValid(s)
print(boo)