'''
Array List를 사용해서 풀어보자

visit()하고 앞에 값들을 지울때 : 시간복잡도 O(n)
forward(), back() 할 때 : 시간복잡도 O(1)
'''

class BrowserHistory(object):
    def __init__(self, hompage):
        self.list = [hompage]
        self.currentIdx = 0
    def visit(self, url):
        # visit하면 앞에 방문기록 지울때 시간복잡도 O(n)
        while(self.currentIdx != len(self.list)-1): # 현재 index 보다 큰 값들은 다 지우기
            self.list.pop()
        self.list.append(url)
        self.currentIdx += 1
        return None
    def back(self, step):
        if(step <= self.currentIdx):
            self.currentIdx -= step
        else:
            self.currentIdx = 0
        return self.list[self.currentIdx]
    def forward(self, step):
        if(self.currentIdx + step < len(self.list)):
            self.currentIdx += step
        else:
            self.currentIdx = len(self.list) - 1
        return self.list[self.currentIdx]

browserHistory = BrowserHistory("leetcode.com")

print(browserHistory.visit("google.com"))
print(browserHistory.visit("facebook.com"))
print(browserHistory.visit("youtube.com"))
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))

print(browserHistory.currentIdx)

print(browserHistory.visit("linkedin.com"))
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))

print(browserHistory.list)