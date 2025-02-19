import sys
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""2

1 1
1
1

3 2
1 3 2
5 5"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline().strip())
text = [line.strip() for line in sys.stdin.readlines() if line.strip()]  # 공백 줄 제거
for i in range(N):
    sejin = sorted(list(map(int, text[(i * 3) + 1].split(' '))), reverse=True)
    sebi = sorted(list(map(int, text[(i * 3) + 2].split(' '))), reverse=True)

    # 최댓값 찾기
    max_sejin = sejin[0]
    max_sebi = sebi[0]

    if sejin[0] >= sebi[0]:
        print("S")
    elif sebi[0] > sejin[0]:
        print("B")
    else:
        print("C")