input_a ="""
       안녕하세요
    문자열의 함수를 공부하자
"""

print(input_a.strip())  # 양쪽 공백 제거
print(input_a.lstrip()) # 왼쪽 공백 제거
print(input_a.rstrip()) # 오른쪽 공백 제거
print(input_a)          # 원본 문자열 출력
print("---중간에 있는 공백 제거---")
print("".join(input_a.split()))  # 중간 공백 제거