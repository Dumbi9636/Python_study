print(True)  # True
print(False)  # False
print(100 == 1000)  # False 
print(100 != 1000)  # True
print(100 < 1000)  # True
print(100 >= 1000)  # False


print("가방" < "하마")  # True
print("가방" > "하마")  # False
# 유니코드(아스키코드) 기준으로 비교한다.
# 한글 사전순서(가나다순)와 동일하다.
# 앞에 있는 것이 더 작은 값을 갖는다. 
# '가'는 44032, '하'는 54616이므로 '가'가 더 작다.
# 따라서 '가방'이 '하마'보다 작다.
# 즉, '가방'이 '하마'보다 사전에서 더 앞에 온다.

# not 연산자 조합
print(not True)  # False
print(not False)  # True
print(not (100 > 50))  # False
print(not (100 < 50))  # True

x= 10
under_20 = x < 20   
print("under_20:", under_20)  # True
print("not under_20:", not under_20)  # False   
