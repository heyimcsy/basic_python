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