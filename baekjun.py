import sys

from collections import defaultdict
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""5
2 4 -10 4 -9"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline().strip())
lists = list(map(int, sys.stdin.readline().split()))
sorted_lists = sorted(set(lists))

list_dict = {value: idx for idx, value in enumerate(sorted_lists)}
print(" ".join(str(list_dict[x]) for x in lists))
# # 테스트 입력을 문자열로 제공
# test_input ="""8
# sbrus.txt
# spc.spc
# acm.icpc
# korea.icpc
# sample.txt
# hello.world
# sogang.spc
# example.txt"""
#
# # sys.stdin을 대체
# sys.stdin = StringIO(test_input)
#
# N = int(sys.stdin.readline().strip())
# files = defaultdict(int)
#
# for _ in range(N):
#     _, ext = sys.stdin.readline().strip().rsplit('.', 1)
#     files[ext] += 1
# for ext in sorted(files):
#     print(ext, files[ext])

# files = {}
# for _ in range(N):
#     text = sys.stdin.readline().split()[0].split('.')[1]
#     if text in files:
#         files[text] += 1
#     else:
#         files[text] = 1
#
# for ext, count in sorted(files.items()):
#     print(ext, count)