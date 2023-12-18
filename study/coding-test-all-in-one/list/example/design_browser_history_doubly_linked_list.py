'''
Doubly linked list를 사용한다
prev

이 문제에서는 head와 tail이 필요가 없어서 지웠다.
'''

class Node(object):
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, hompage):
        self.current = Node(value=hompage)
        return None
    def visit(self, url):
        self.current.next = Node(value=url, prev=self.current)
        self.current = self.current.next
        return None
    def back(self, step):
        for _ in range(step):
            if(self.current.prev):
                self.current = self.current.prev
            else:
                break
        return self.current.value
    def forward(self, step):
        for _ in range(step):
            if(self.current.next):
                self.current = self.current.next
            else:
                break
        return self.current.value

browserHistory = BrowserHistory("leetcode.com")
print(browserHistory.visit("google.com"))
print(browserHistory.visit("facebook.com"))
print(browserHistory.visit("youtube.com"))
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))
print(browserHistory.visit("linkedin.com"))
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))