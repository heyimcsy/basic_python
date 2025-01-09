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

for person in people:
    name = person['name']
    age = person['age']
    if age >= 25:
        print(name,'s age is', age)