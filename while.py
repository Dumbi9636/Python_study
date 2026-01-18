# 범위 자료형

range(A)
range(A, B)
range(A, B, C)

# A부터 B-1까지 C 간격의 숫자 생성
# 숫자는 0부터 시작
# 알파벳은 A부터 시작
a = range(5)
print(a)  # range(0, 5)
# 위 a 안에 들어있는 값을 보려면 list() 함수를 사용
list(range(a))  # [0, 1, 2, 3, 4]

list(range(5, 10))  # [5, 6, 7, 8, 9]

# 주의 할 점은 range(5, 10) 은 5부터 9 까지의 숫자를 생성한다는 것이다
# 즉, 두 번째 숫자는 포함되지 않는다 (B-1 까지 생성)
# 또한 range() 함수 안에는 정수만 들어갈 수 있다. 실수나 문자열이 들어가면 TypeError 가 발생한다

# for 반복문: 범위와 함께 사용하기 
for i in range(5):
    print(i)  # 0 1 2 3 4
# 위 예시는 0부터 4까지의 숫자를 차례대로 출력한다

# for 반복문: 리스트와 범위 조합하기
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i])
    # apple
    # banana
    # cherry
# 위 예시는 리스트의 길이만큼 반복하면서 각 인덱스에 해당하는 값을 출력한다
# 위 예시에서 len() 함수는 리스트의 길이를 반환한다. 
# len() 을 사용하지 않는다면 typeError 가 발생할 것이다

# for 반복문: 반대로 반복하기
# 역 반복문
for i in range(4, 0 -1, -1):
    print(i)
    # 4
    # 3
    # 2
    # 1
    # 0
# 위 예시는 4부터 0까지 역순으로 숫자를 출력한다
# range(4, -1, -1) 은 4부터 -1 까지 -1 간격으로 숫자를 생성한다
# range()는 최대 3개의 인자만 받습니다.
# 세 번째 인자는 생략할 수 있으며, 생략할 경우 기본값은 1입니다.
# 따라서 range(5) 는 range(0, 5, 1) 과 동일합니다.


# reversed() 함수와 함께 사용하기
for i in reversed(range(5)):
    print(i)
    # 4
    # 3
    # 2
    # 1
    # 0 
# 위 예시는 reversed() 함수를 사용하여 0부터 4까지의 숫자를 역순으로 출력한다

# 중첩 반복문으로 피라미드 만들기
output = ""

for i in range(1, 10):
    for j in range(0, i):
        output += "*"
    output += "\n"
print(output)
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# 위 예시는 중첩 반복문을 사용하여 피라미드 모양의 별을 출력한다

# While 반복문
while True:
    #"." 을 출력
    # 기본적으로 end 가 "\n" 이기 때문에 줄바꿈이 일어난다
    # 빈 문자열 "" 을 end 로 지정하면 줄바꿈이 일어나지 않는다
    print(".", end="")
    # 무한 루프를 방지하기 위해 break 문을 사용
    break
# 위 예시는 while 반복문을 사용하여 "." 을 출력한다

# While 반복문: for 반복문처럼 사용하기
i = 0
while i < 5:
    print(i)  # 0 1 2 3 4
    i += 1
# 위 예시는 for 반복문과 동일하게 0부터 4까지의 숫자를 출력한다

# While 반복문: 상태를 기반으로 반복하기
list_test = [1, 2, 1, 2]
value = 2
# list_test 내부에 value 가 제거될 때까지 반복
while value in list_test:
    list_test.remove(value)
print(list_test)  # [1, 1]

# while 반복문: 시간을 기반으로 반복하기
import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
print("5초 동안 반복한 횟수:{}".format(number))


# While 반복문: break 키워드, continue 키워드
i = 0
while True:
    print("{}번째 반복".format(i))  
    i += 1
    # 반복 종료
    input_text = input("종료하시겠습니까? (y/n): ")
    if input_text == 'y':
        print("반복을 종료합니다.")
        break

# continue 키워드 사용 예시
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number < 5:
         # number 가 5 미만일 경우 다음 반복으로 넘어감
        continue 
    print("5 이상의 숫자:", number)
    # 출력
    # 5 이상의 숫자: 5

