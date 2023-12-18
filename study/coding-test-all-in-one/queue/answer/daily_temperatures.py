class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0] * len(temperatures) # 모두 0으로 초기화

        ''' for문에서 사용하는 enumerate 함수
        >>> for i, letter in enumerate(['A', 'B', 'C']):
        ...     print(i, letter)
        0 A
        1 B
        2 C
        '''
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and cur_temp > stack[-1][1]: 
                prev_day, _ = stack.pop() # tuple을 사용하여 날짜만 저장
                answer[prev_day] = cur_day - prev_day
            stack.append((cur_day, cur_temp))
        return answer

solution = Solution()
answer = solution.dailyTemperatures([71, 69, 67, 65, 69, 69, 71])
print(answer)


'''
우리가 시간복잡도를 계산할 때, 이중 반복문이 있으면 n^2이겠거니 많이 생각을 하죠.
그런경우는 다음과 같은 상황이에요.
for i = 1 ~ n :
for j = 1 ~n:
이런경우 의심할 여지없이 n^2번 실행되서 시간복잡도는 O(n^2)입니다.

근데 반복문이 이중으로 쓰이긴 했는데, 매 순간 n번 반복하지 않을 때가 있어요. 보통 for + while형태로 많이 출몰합니다.
for i = 1~n :
while 조건문:

이 경우 for 반복문은 n번 반복 되는건 맞죠. 하지만 for문이 한 번 반복할 때 while문을 한번 실행할 텐데, while문은 몇번 반복할지 모르는 상황이요! 그래서 하나씩 따져봐야돼요.
stack에는 저장할 수 있는 데이터가 총 n개의 데이터 뿐이에요. n개의 데이터를 중복해서 stack에 저장할 수 는 없어요. 그러니까 결국 stack에 들어왔다가 나오는(push -> pop)할 수 있는 횟수는 아무리 많아도 n번이겠죠.
즉 for 반복문이 n번 진행되는 와중에 while문은 "총" n번만 실행되는거에요.
--> 결론 : 시간복잡도 O(n)
'''