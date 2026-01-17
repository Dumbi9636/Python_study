# 아직 구현하지 않은 부분은 NotImplementedError 예외를 강제로 발생시키게 할 수 있다. 

number = input("숫자 입력: ")
number = int(number)  # 입력받은 문자열을 정수로 변환

if number > 0:
    # 양수일때: 아직 미구현
    raise NotImplementedError("양수 처리 기능은 아직 구현되지 않았습니다.")
else:
    # 음수일때: 아직 미구현
    raise NotImplementedError("음수 처리 기능은 아직 구현되지 않았습니다.")

