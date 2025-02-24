from io import StringIO
import sys

# 백준 2908
test_input = """734 893"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)


def swap_digits(x):
    num_list = list(str(x))
    num_list[0], num_list[2] = num_list[2], num_list[0]
    return int("".join(num_list))

numbers = list(map(swap_digits, sys.stdin.readline().split()))

print(max(numbers))
