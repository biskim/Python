"""
관계연산자
"""

# 1 동등 비교

num1 = 100 # 피연산자
num2 = 20  # 피연산자2

bool_result = num1 == num2  # bool은 자료형이고 result는 변수이름 2개를 하나로 붙임
print(bool_result)

bool_result = num1 != num2 # 두 변수의 값이 다르다
print(bool_result)

# 2 크기 비교
bool_result = num1 > num2
print(bool_result)
bool_result = num1 >= num2
print(bool_result)
bool_result = num1 < num2
print(bool_result)
bool_result = num1 <= num2
print(bool_result)