'''
Stack : 후입선출 LIFO(Last In First Out)
Array List라고 생각하면 된다.
'''

# stack 선언
s = []

# push - 시간복잡도 : O(1)
s.append(1)
s.append(2)
s.append(3)

# pop - 시간복잡도 : O(1)
s.pop() # [1, 2]
s.pop() # [1]

print(s)