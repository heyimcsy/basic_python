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

email = myemail.split('@')[1].split('.')[0]

print(email)