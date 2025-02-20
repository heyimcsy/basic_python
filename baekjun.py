import sys
from io import StringIO

import calendar as cd

# 백준 2753
test_input ="""2401"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

Y = int(sys.stdin.readline())


print(1 if cd.isleap(Y) else 0)