a = ('사과', '감', '배', '포도')

# a[1] = '수박' 해당 식처럼 내용을 바꾸면 에러가 난다.
print(a)

b = [1,2,5,3,2,5,2,7,4,2,4,1]
b_set = set(b)
# 중복값을 삭제해준다.
print(b_set)

# 차집합 교집합 합집합

c = ['사과', '감', '베', '수박', '딸기']
d = ['배', '사과', '포도', '참외', '수박']

c_set = set(c)
d_set = set(d)

print(c_set)
print(d_set)

print(c_set & d_set)
print(c_set | d_set)

student_a = set(['물리2','국어','수학1','음악','화학1','화학2','체육'])
student_b = set(['물리1','수학1','미술','화학2','체육'])

print(student_a - student_b)

scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}
]

for s in scores:
    name = s['name']
    score = s['score']
    print(name + '의 점수는 ' + str(score) + '점입니다.')
    print(f'{name}의 점수는 {score}점입니다.')

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 35}
]

# bobby 가 age가 없으면 ?
for person in people:
    try:
        if person['age'] > 20:
            print(person['name'])
    except:
        print(person['name'], '에러입니다')


num = 3

result = ('짝수' if num % 2 == 0 else '홀수')

print(f'{num}은 {result}입니다.')

a_list = [1,3,2,5,1,2]

b_list = [a * 2 for a in a_list]

print(b_list)