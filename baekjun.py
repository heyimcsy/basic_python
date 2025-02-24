from io import StringIO
import sys

# 백준 11720
test_input = """11
10987654321"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())
number = sys.stdin.readline().strip()
sum_number = 0
for i in range(N):
    sum_number += int(number[i])
print(sum_number)