money = 3000

if money > 3800:
    print('택시를 타자')
elif money > 1200:
    print('버스를 타자!')
else:
    print('걸어가자!')

print('일단 집에 가자')

fruits = ['apple', 'banana', 'kiwi', 'strawberry', 'melon']

for fruit in fruits:
    print(fruit)

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    if age >= 25:
        print(i, name,'s age is', age)
    if i > 3:
        break


num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

# 짝수 띄우기
# count = 0
# for num in num_list:
#     if num % 2 == 0:
#         count = count + 1
# print(count)

# 전체 수 더하기
# totalSum = 0
# for num in num_list:
#     totalSum = totalSum + num
# print(totalSum)

# 가장 큰 수
num_list.sort(reverse=True)

print(num_list[0])