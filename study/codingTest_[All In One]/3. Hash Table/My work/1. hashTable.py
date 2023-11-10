score = {
    'kor': 88,
    'eng': 55,
    'math': 96
}

print(score)

print(score['kor'])

## 값 변경
score['eng'] = 77
print(score['eng'])

## 값 추가
score['sci'] = 100
print(score['sci'])

## key 있는지 확인
print('music' in score)
# False


## in : dictionary에 key가 존재하는지 확인 
if 'music' in score:
    print(score['music'])
else:
    score['music'] = 0


## dictionary
student_info = {
    2022390: '이돈훈',
    2022392: '이선언',
    2022394: '나찬곤',
    2022400: '김헝존'
}

## dictionary.items()
for id, name in student_info.items():
    print(id, name)

## dictionary.keys()
for id in student_info.keys():
    print(id)

## dictionary.values()
for name in student_info.values():
    print(name)

## dictionary.get()
myName = student_info.get(2022394)
print('내 이름은', myName)

## dictionary.get() 없는 값을 가져올 때
print(student_info.get(1234))
# None

## dictionary.get() 값이 없으면 초기화
print(student_info.get(111, '홍길동'))
# 홍길동

## dictionary.get() 응용
a = {}
if 3 not in a:
    a[3] = 1
else:
    a[3] += 1
print(a[3])


b = {}
# 위와 같은 코드를 한 줄로 변경
b[3] = 1 + b.get(3, 0)
print(b[3])




# in 테스트
test = {
    1: 'a',
    2: 'b',
    'c': 3
}

print(1 in test.keys())
print(2 in test.keys())

print(3 in test.values())

print(2 in test) # True -> key값을 비교
print(3 in test) # False -> key에 없음