# 파이썬에서 if 조건문은 다음과 같이 작성합니다.
# if 조건문 뒤에는 반드시 콜론(:)이 와야 합니다.
# if 문 다음 4칸 들여쓰기 (스페이스 4칸 또는 탭 1칸) 후에 실행할 코드를 작성합니다.


if True:
    print("조건이 참일 때 실행됩니다.")
    print("여러 줄도 가능합니다.")
else:
    print("조건이 거짓일 때 실행됩니다.")

# 입력을 받는다
number = input("숫자를 입력하세요: ")
numnber = int(number)  # 입력받은 문자열을 정수로 변환

# 양수 조건
if number > 0:
    print("입력한 숫자는 양수입니다.")

# 음수 조건
if number < 0:
    print("입력한 숫자는 음수입니다.")

# 0 조건
if number == 0:
    print("입력한 숫자는 0입니다.")

# 짝수 조건 
if number % 2 == 0:
    print("입력한 숫자는 짝수입니다.")

# 홀수 조건
if number % 2 != 0:
    print("입력한 숫자는 홀수입니다.")


# 날짜, 시간 활용하기
import datetime

# 현재 날짜/ 시간 구하기
now = datetime.datetime.now()

# 출력
print(now.year)   # 연도
print(now.month)  # 월
print(now.day)    # 일
print(now.hour)   # 시
print(now.minute) # 분
print(now.second) # 초

# 현재 시간이 오전인지 오후인지 판단
if now.hour < 12:
    print("현재 시간은 오전입니다.")
if now.hour >= 12:
    print("현재 시간은 오후입니다.")

# 현재 요일 판단
# 파이썬에서 요일은 월요일(0)부터 일요일(6)까지 숫자로 표현됩니다.
if now.weekday() == 0:
    print("오늘은 월요일입니다.")   
if now.weekday() == 1:
    print("오늘은 화요일입니다.")
if now.weekday() == 2:
    print("오늘은 수요일입니다.")

# format 함수를 사용하여 날짜/시간을 한줄로 출력하기
import datetime

now = datetime.datetime.now()

print("{}년, {}월, {}일, {}시, {}분, {}초".format(
    now.year, now.month, now.day,
    now.hour, now.minute, now.second
))

