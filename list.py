array = [273, 32, 103, "문자열", True, False]

print(array)    # [273, 32, 103, '문자열', True, False]
print(array[0]) # 273
print(array[3]) # 문자열
print(array[-1])# False
print(array[-3])# 103
print(len(array)) # 6

# array[1] 값을 1000으로 변경하기
array[1] = 1000
print(array)    # [273, 1000, 103, '문자열', True, False]

# 2개의 값을 꺼내오기
list_a = [10, 20, 30, '문자열', 50, 60]
list_a[-1]
60
list_a[-2]
50
list_a[-3]
'문자열'

list_a[3][1]
'문'
list_a[3][2]
'자'
list_a[3][3]
'열'
# list_a[3] 을 지정하면 "문자열" 전체가 나오고,
# list_a[3][n] 으로 지정하면 "문자열"에서 n번째 글자가 나온다.

# 리스트에서의 IndexError
print(list_a[10])  # IndexError: list index out of range
# 리스트의 인덱스 범위를 벗어난 값을 지정하면 IndexError 가 발생한다.

# 리스트 연결하기
list_c = [1, 2, 3]
list_d = [4, 5, 6]

print("#리스트")

print("list_c=", list_c)
print() 

print("list_d", list_d)
print()

# 기본 연산자
print("list_c + list_d =", list_c + list_d)  # [1, 2, 3, 4, 5, 6]
print("list_c * 3 =", list_c * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print("len(list_c) =", len(list_c))  # 3

# 리스트에 요소 추가하기
# append 함수 사용하기
list_e = [1, 2, 3]
list_e.append(4)
print("list_e after append(4):", list_e)  # [1, 2, 3, 4]
# insert 함수 사용하기
print("# 리스트 중간에 요소 추가하기")
list_e.insert(0,10)
print("list_e after insert(0,10):", list_e)  # [10, 1, 2, 3, 4]
# insert 를 사용하면 괄호 안에서 정해 준 위치에 요소를 삽입하여 해당 위치의 요소는 뒤로 하나 씩 밀린다.

# extend 함수 사용하기
# extend 함수를 사용하면 리스트에 여러 요소를 한꺼번에 추가할 수 있다.
print("# 리스트에 여러 요소 추가하기")
list_e.extend([20,30])
print("list_e after extend([20,30]):", list_e)  # [10, 1, 2, 3, 4, 20, 30]
# extend 함수는 인덱스의 마지막 요소 위치에 추가된다.

# 리스트에서 요소 제거하기
print("# 리스트에서 요소 제거하기")

# del 함수 사용하기
del list_e[0]
print("list_e after del list_e[0]:", list_e)  # [1, 2, 3, 4, 20, 30]
# del 함수는 지정한 위치의 요소를 제거한다.

# pop 함수 사용하기
list_e.pop(2)
print("list_e after pop(2):", list_e)  # [1, 2, 4, 20, 30]
# pop 함수는 지정한 위치의 요소를 제거하고 제거한 요소를 반환한다.
# 인덱스를 지정하지 않으면 마지막 요소를 제거한다.

# 범위를 지정해 리스트의 요소를 한꺼번에 제거하기
list_e[1:3] = []
print("list_e after list_e[1:3] = []:", list_e)  # [1, 20, 30]
# 리스트에서 인덱스의 범위를 지정하여 빈 리스트[]를 대입하면
# 지정한 범위의 요소가 한꺼번에 제거된다.


# 리스트 슬라이싱
# 리스트 슬라이싱에서 [시작 인덱스:끝 인덱스] 형태로 지정하면
# 시작 인덱스부터 끝 인덱스-1 까지의 요소를 꺼내올 수 있다.
# 주의할 점은 끝 인덱스의 위치에 있는 요소는 포함되지 않는다는 것이다.
# 예를 들어, list_f[2:5] 라고 지정하면
# 인덱스 2, 3, 4 위치에 있는 요소가 꺼내와지고
# 인덱스 5 위치에 있는 요소는 포함되지 않는다.
list_f = [10, 20, 30, 40, 50, 60, 70, 80, 90]   
print("# 리스트 슬라이싱")
print("list_f[2:5]:", list_f[2:5])  # [30, 40, 50]
print("list_f[:4]:", list_f[:4])    # [10, 20, 30, 40]


# 리스트 내부 요소 모두 제거하기
list_f.clear()
print("list_f after clear():", list_f)  # []
# 리스트가 비어있는지 확인하기
print("len(list_f) == 0:", len(list_f) == 0)  # True
# 또는
print("list_f == []:", list_f == [])  # True
# 리스트가 비어있는지 확인하는 방법은 두 가지가 있다.
# len 함수를 사용하여 리스트의 길이가 0인지 확인하거나
# 리스트가 빈 리스트[]와 동일한지 확인하는 방법이다.

# 리스트 정렬하기
list_g = [30, 10, 50, 20, 40]
print("# 리스트 정렬하기")
list_g.sort()
print("list_g after sort():", list_g)  # [10, 20, 30, 40, 50]
# sort 함수는 리스트의 요소를 오름차순으로 정렬한다.
list_g.sort(reverse=True)
print("list_g after sort(reverse=True):", list_g)  # [50, 40, 30, 20, 10]
# reverse=True 옵션을 지정하면 내림차순으로 정렬한다.

# 리스트 역순으로 뒤집기
list_g.reverse()
print("list_g after reverse():", list_g)  # [10, 20, 30, 40, 50]
# reverse 함수는 리스트의 요소 순서를 역순으로 뒤집는다.
# 정렬된 리스트에 reverse 함수를 사용하면 정렬된 순서의 반대가 된다.

# 리스트 내부에 있는지 확인하기 in/not in 연산자
list_h = [10, 20, 30, 40, 50]
print("# 리스트 내부에 있는지 확인하기")
print("30 in list_h:", 30 in list_h)  # True
print("100 in list_h:", 100 in list_h)  # False

# not in 연산자 사용하기
print("30 not in list_h:", 30 not in list_h)  # False
print("100 not in list_h:", 100 not in list_h)  # True
# in 연산자는 리스트 내부에 지정한 값이 있는지 확인하여
# not in 연산자는 리스트 내부에 지정한 값이 없는지 확인한다.

# for 반복문: 리스트와 함께 사용하기
array = [273, 32, 103, "문자열", True, False]
for element in array:
    print(element)
# 리스트의 요소를 하나씩 꺼내와서 element 변수에 담아 반복 실행한다.
# 출력 결과:
# 273
# 32
# 103
# 문자열
# True
# False

# 중첩 리스트와 중첩 반복문
list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# for 반복문을 중첩해서 사용
for items in list_of_lists:
    print(items)

    for item in items:
        print(item)
# 출력 결과:
# [1, 2, 3]
# 1
# 2 
# 3
# [4, 5, 6]
# 4
# 5
# 6
# [7, 8, 9]
# 7
# 8
# 9

# 전개연산자
list_a = [1, 2, 3]
list_b = [list_a, *list_a]
print("list_b =", list_b)  # [1, 2, 3, 1, 2, 3]
# 전개 연산자(*)를 사용하여 리스트의 요소를 풀어서
# 새로운 리스트를 만들 때 사용할 수 있다.




