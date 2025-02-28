import math
from io import StringIO
import sys
import heapq

# 백준 28702
test_input = """Fizz
13
14"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
third = sys.stdin.readline().strip()

number = 0
if first.isdigit():
    number = int(first) + 3
elif second.isdigit():
    number = int(second) + 2
elif third.isdigit():
    number = int(third) + 1

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)