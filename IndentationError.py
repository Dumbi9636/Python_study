# indentation error 예제
# 들여쓰기가 올바르지 않을 때 발생하는 오류
# 파이썬은 들여쓰기를 통해 코드 블록을 구분하므로, 들여쓰기가 맞지 않으면 IndentationError가 발생함
# 예를 들어, if 문 다음에 오는 코드 블록이 들여쓰기가 맞지 않으면 오류가 발생함


number = input("숫자 입력: ")
numnber = int(number)  # 입력받은 문자열을 정수로 변환

if number > 0:
    # 양수일때: 아직 미구현
    0
else:
    # 음수일때: 아직 미구현
    0

    # pass 한 키워드에 임시적으로 0을 넣어서 에러가 나지 않도록 함
    

# 나중에 코드를 작성할 때 pass 키워드를 사용하여 빈 블록을 채울 수 있음 
if number > 0:
    # 양수일때: 아직 미구현
    pass
else:
    # 음수일때: 아직 미구현
    pass