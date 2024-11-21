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
