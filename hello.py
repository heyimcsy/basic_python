a = '나는 호구다'
b = a + ' 배고프다'

# str 숫자를 string으로 변환해주는 함수
c = str(2)
d = c + '숫자와 문자의 합침은 에러'

print(b)

print(d)

text = 'abcdefghijk'
# result = len(text)
# result = text[:3]
# result = text[3:]
# result = text[:] 복사
result = text[3:7]

print(result)

myemail = 'abc@sparta.com'

email = myemail.split('@')[1].split('.')[0][:3]
print(email)

phone = '02-123-1234'

phoneResult = phone.split('-')[0]

print(phoneResult)

# list 순서가 중요하게 값을 담는다.
# 딕셔너리는 키벨류로 값을 담는다.

a_list = ['사과', '배', '감']
a_list.append('수박')

result_a = ('사과' in a_list)

b_dict = {'name': 'bob', 'age': 30, 'job': 'engineer'}

b_dict['age'] = 50
b_dict['height'] = 155

result_b = b_dict

print(result_b)

# people = [{'name' : 'jon', 'age': 20}, {'name': 'jisoo', 'age': 17}]
#
# people.append(b_dict)
# print(people)

people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

# smith의 과학 점수
print(people[2]['score']['science'])