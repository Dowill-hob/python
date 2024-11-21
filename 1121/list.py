'''
number = [1, 5, 3, 4, 8, 2, 3, "Hello", "python"]
print(number[3])  # 4

text = "Hello, Python"
text = list(text)
print(text)
'''
'''
# 리스트 슬라이스
shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식키보드"]]
print(shop[:2])
print(shop[3])
print(shop[-2])
shop[0] = "긴팔"
print(shop)

# shop[100] = "신발"
# print(shop)

del shop[1]
print(shop)
del shop[2:]
print(shop)

a = [1, 2, 3]
b = ["안녕하세요", "반갑습니다"]
print(a + b)
print(b * 3)
'''
'''
# 정렬함수
num = [3, 1, 5, 2]
num_asc = sorted(num)
print(num_asc)
num_desc = sorted(num, reverse=True)
print(num_desc)
print(num)
'''
'''
num = [3, 1, 5, 2]
num.sort()  # 매서드
print(num)

korean = ["강", "이", "박", "최", "김"]
korean.sort
print(korean)
korean.sort(reverse=True)
print(korean)

alphabet = ["b", "c", "a", "d"]
alphabet.reverse()
print(alphabet)
print(alphabet.index('c'))
print(alphabet.index('w')) # 오류
'''
'''
a = ["a", "b", "c", "안녕", "Hi"]
a.append("python")
print(a)
a.pop()
print(a)
a.pop(3)
print(a)
a.remove('a')
print(a)
a.insert(2, 'a')
print(a)
a.clear()
print(a)
'''
'''
x = ["q", 'w', 'e', 'r', 'w']
print(x.count('w'))
'''
'''
# 실습.리스트 연습문제
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(rainbow[2])
rainbow_asc = sorted(rainbow)
print(rainbow_asc)
rainbow.append("coral blue")
print(rainbow)
del rainbow[3:7] ##### 생각에 넣어놓기
print(rainbow)
'''
'''
# 이차원 리스트
# 3*3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2][0])
# 요소 추가
matrix[1] = matrix[1] + [99]
print(matrix)
# 행 추가
matrix = matrix+[[10, 11, 12]]
print(matrix)
# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 5000
print(matrix)
# 행 삭제
del matrix[2]
print(matrix)
# 행 개수
rows = len(matrix)
print(rows)
# 열 개수
cols = len(matrix[0])
print(cols)
'''
'''
# 이차원 매서드
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 요소 추가
matrix[0].append(10)
print(matrix)
# 행 추가
matrix.append([10, 11, 12])
print(matrix)
matrix[1].insert(1, 100)
print(matrix)
matrix.insert(2, ["안녕하세요", "반갑습니다", "어서오세요"])
print(matrix)

# 확장
matrix[0].extend([11, 12])
print(matrix)
'''

t1 = (1,)  # tuple에서는 요소 1개만 있을때 ',' 필수
t2 = (1, 2, 3, 4, 5, 6, 3, 3, 3)
t3 = 1, 2, 3
t4 = ('a', 'b', 'c', ("Hi", "thanks"))
print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])
print(len(t4))
print('c' in t4)
