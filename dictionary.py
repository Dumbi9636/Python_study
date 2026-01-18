# dictionary 는 '키'와 '값'의 쌍으로 이루어진 자료형으로 데이터를 저장한다

dict_a = {'name': ['Alice', 'john', 'kai'], 'age': 30, 'city': 'New York'}

print(dict_a)  # {'name': ['Alice', 'john', 'kai'], 'age': 30, 'city': 'New York'}

# dictionary 에서 값에 접근하려면 [] 대괄호 안에 키 값을 사용한다
# javascript 의 object 와 유사하다
print(dict_a['name'])  # ['Alice', 'john', 'kai']
print(dict_a['age'])   # 30
print(dict_a['city'])  # New York


# 값을 변경하기
dict_a['age'] = 31
print(dict_a)  # {'name': ['Alice', 'john', 'kai'], 'age': 31, 'city': 'New York'}

# name 은 dict_a 의 키 이기도 하지만 여러 개의 자료를 가지고 있는 리스트이기도 하므로 다음과 같이 인덱스를 지정하여
# 리스트 안의 특정 값을 출력할 수도 있다
dict_a['name']
dict_a['name'][0]  # 'Alice'
dict_a['name'][1]  # 'john'
dict_a['name'][2]  # 'kai'

# dictionary 를 만들때 입력 실수를 하는 경우가 있다. 이러한 오류에는 NameError, TypeError, KeyError 등이 있다

# KeyError : 존재하지 않는 키를 사용하려고 할 때 발생하는 오류
# print(dict_a['country'])  # KeyError: 'country'

# TypeError : dictionary 자료형에서 인덱스로 접근하려고 할 때 발생하는 오류
# print(dict_a[0])  # TypeError: unhashable type: 'list

# NameError : dictionary 자료형이 정의되지 않았을 때 발생하는 오류
# print(dict_b)  # NameError: name 'dict_b' is not defined

# dictionary 에 새로운 키-값 쌍 추가하기
dict_a['country'] = 'USA'
print(dict_a)  # {'name': ['Alice', 'john', 'kai'], 'age': 31, 'city': 'New York', 'country': 'USA'}

# dictionary 에서 키-값 쌍 삭제하기
del dict_a['city']
print(dict_a)  # {'name': ['Alice', 'john', 'kai'], 'age': 31, 'country': 'USA'}

#KeyError 발생 예시
# 리스트의 길이를 넘는 인덱스에 접근하면 IndexError 가 발생하는 것 처럼, 딕셔너리도 존재하지 않는 키에 접근하게 되면 에러가 발생한다
dictionary = {}
dictionary['key']  # KeyError: 'key'

# 제거할때도 마찬가지로 ㅈ존하지 않는 키를 제거하려고 하면 KeyError 가 발생한다
del dictionary['key']  # KeyError: 'key'

# 이러한 에러를 방지하기 위해서는 in 키워드를 사용하여 해당 키가 딕셔너리에 존재하는지 확인할 수 있다
if 'key' in dictionary:
    print(dictionary['key'])
else:
    print("키가 존재하지 않습니다.")

#get() 함수 
# 딕셔너리의 get() 메서드를 사용하면 KeyError 없이 안전하게 값을 가져올 수 있다
# 존재하지 않는 키에 접근할 경우 None 을 반환하거나, 두 번째 인자로 지정한 기본값을 반환한다
value = dictionary.get('key', '기본값')
print(value)  # 기본값
# 위 예시에서 'key' 가 딕셔너리에 없기 때문에 '기본값' 이 출력된다
# 2번째 인자인 '기본값' 을 생략하면 None 이 반환된다

# for 반복문 dictionary 와 함께 사용하기
dict_b = {'a': 1, 'b': 2, 'c': 3}

for key in dict_b:
    #출력
    print(key, ":", dict_b[key])
    # a : 1
    # b : 2
    # c : 3
# 위 예시에서 for 반복문은 dict_b 의 각 키를 순회하며, 각 키에 해당하는 값을 출력한다
# key는 딕셔너리에 저장된 값이 아니라 for문이 매 반복마다 새로 만들어서 값을 담는 변수다.



