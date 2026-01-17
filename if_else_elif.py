# if 조건문에 else 구문을 추가해서 짝수와 홀수 구분하기
number = input("정수 입력: ")
number = int(number)

# 조건문 사용
if number % 2 == 0:
    print("입력한 숫자는 짝수입니다.")
else:
    print("입력한 숫자는 홀수입니다.")



# elif 구문 사용하기

import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")


# 변수 선언
score = float(input("학점 입력: "))

# 조건문 작성
if score >= 4.5:
    print("A+ 학점입니다.") 
elif 4.0 <= score < 4.5:
    print("A 학점입니다.")  
elif 3.5 <= score < 4.0:
    print("B+ 학점입니다.")
elif 3.0 <= score < 3.5:
    print("B 학점입니다.")
elif 2.5 <= score < 3.0:
    print("C+ 학점입니다.")
elif 2.0 <= score < 2.5:
    print("C 학점입니다.")
elif 1.5 <= score < 2.0:
    print("D+ 학점입니다.")
elif 1.0 <= score < 1.5:
    print("D 학점입니다.")
else:
    print("F 학점입니다.")

# 조건문 작성(상위 조건 중복 검사 제거)
if score >= 4.5:
    print("A+ 학점입니다.")
elif score >= 4.0:
    print("A 학점입니다.")  
elif score >= 3.5:
    print("B+ 학점입니다.")
elif score >= 3.0:
    print("B 학점입니다.")
elif score >= 2.5:
    print("C+ 학점입니다.")
elif score >= 2.0:
    print("C 학점입니다.")
elif score >= 1.5:
    print("D+ 학점입니다.")
elif score >= 1.0:
    print("D 학점입니다.")
else:
    print("F 학점입니다.")

