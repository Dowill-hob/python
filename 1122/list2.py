'''
# set
s1 = {1, 1, 1, 1, 1, 1, 1, 1, 2}
print(s1)
s2 = ['안녕', '잘가', 'Hi', 'Hi']
print(s2)
print(set(s2))
'''
'''
s1 = {1, 2, 3, 3, 4}
print(s1)
s1.add(5)
print(s1)
s1.update([6, 7, 8, 9, 10])
print(s1)
s1.remove(3)  # 없는 내용을 삭제시 오류 출력
print(s1)
s1.discard(9)  # 없는 내용을 삭제하여도 오류 값을 출력하지 않음
print(s1)
s1.clear()
print(s1)
'''
'''
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# 합집합
s3 = s1 | s2
print(s3)
s3 = s1.union(s2)
print(s3)

# 교집합
s3 = s1 & s2
print(s3)
s3 = s1.intersection(s2)
print(s3)

# 차집합
s3 = s1 - s2
print(s3)
s3 = s1.difference(s2)
print(s3)
'''
'''
# dictionary
# 생성
dict1 = {}
dict1 = dict()
print(dict1)
dict1 = {
    "name": "김준식",
    "age": 25,
    "city": "서울",
    "hobby": ["런닝", "등산", "헬스"]
}
print(dict1)
dict2 = dict(name="김준식", age=25)
print(dict2)
print(dict1['name'])
print(dict1['hobby'])

# 값 수정
dict1["age"] = 21
print(dict1)
# 값 추가
dict1["birthday"] = 20001011
dict1['hobby'] = ['런닝', '등산', '헬스', "캠핑"]
print(dict1)
del dict1['birthday']
print(dict1)
'''
'''
# 딕셔너리 메서드
fruits = {
    'apple': '사과',
    'banana': '바나나'
}
print(fruits.get('apple'))
print(fruits.get('peach'))
print(fruits.get('peach', '복숭아'))

# 여러요소 추가
fruits.update({
    'grapes': '포도',
    'melon': '멜론'
})
print(fruits)
print(fruits.keys())
print(fruits.values())
print(fruits.items())
fruits.clear()
print(fruits)
'''
'''
# 실습.딕셔너리
# 1
dict1 = {}
# 2
dict1 ={   
    'Alice': 85,
    'Bob': 90,
    'Charlie': 90
}
# 3
dict1.update({'David': 80})
# 4
dict1['Alice'] = 88
# 5
del dict1['Bob']
'''

# 내장함수
# sum()
'''
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

scores = {"국어": 90, "영어": 80, "수학": 85}
print(sum(scores.values()))
'''
# zip()
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [85, 90, 88, 95]
zipped = list(zip(names, scores))
print(zipped)
