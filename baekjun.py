import sys
from collections import Counter

from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""0 1 0 1
1 1 1 0
0 0 1 1"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

# 코드 실행
text = sys.stdin.read().splitlines()
print(text)

for n in text:
    print(n.count('0'))
    if n.count('0') == 1:
        print('A')
    elif n.count('0') == 2:
        print('B')
    elif n.count('0') == 3:
        print('C')
    elif n.count('0') == 4:
        print('D')
    else:
        print('E')
# N, M = map(int, text[0].split(' '))
# students = []
#
# for i in range(N):
#     number = int(text[(i * 2)+1])
#     studentNumbers = tuple(text[(i * 2) + 2].split(' '))
#     students.extend(studentNumbers)
# count = Counter(students)
# print(count)
# counts = sum(1 for value in count.values() if value >= M)
# print(counts)









# count, food, used = text
# count = int(count)
# food = list(food.split(' '))
# used = list(used.split(' '))
#
# used_dict = {item: True for item in used}
# for item in food:
#     if item not in used_dict:
#         print('2222',item)



# fruits = {'BANANA': 0, 'PLUM': 0, 'LIME': 0, 'STRAWBERRY': 0}
# for i in range(int(text[0])):
#     fruit, count = text[i + 1].split(' ')
#     fruit = str(fruit)
#     count = int(count)
#     if fruit in fruits:
#         fruits[fruit] = fruits[fruit] + count
#         print(fruits)
# if 5 in fruits.values():
#     print('YES')
# else:
#     print('NO')

#

# print(ord('b') - 96)

