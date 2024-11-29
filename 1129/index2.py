# 파일 입출력

with open("test.txt", "w", encoding="utf-8") as file:
    file.write("안녕하세요\n")
    file.write("파이썬 쓰기연습\n")


# 파일 추가
with open("test.txt", 'a', encoding="utf-8") as file:
    file.write("내용추가\n")
    file.write("1111\n")

lines = ["첫번째\n", "두번째\n", "세번째\n"]
with open("test.txt", "a", encoding="utf-8") as file:
    file.writelines(lines)

with open("user.txt", "w", encoding="utf-8") as file:
    while True:
        line = input("파일에 넣을 문자열 입력(종료하려면 '종료' 입력): ")
        if line == "종료":
            print("입력을 종료합니다")
            break
        file.write(line + "\n")

# 파일 읽기
with open("user.txt", "r", encoding="utf-8") as file:
    print(file.read())
with open("user.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open("user.txt", "r", encoding="utf-8") as file:
    print(file.readlines())

with open("user.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

with open("user.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for idx, value in enumerate(lines):
        print(f"{idx}인덱스값은 {value.strip()}입니다.")
