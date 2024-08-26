# 백준 1149 문제

# 집의 수
N = int(input("N의 개수를 입력하시오 : "))
# Home list
homes_colors = [[] for _ in range(N)]

# N개의 집에 대한 3개 색의 비용 입력
for i in range(N):
    homes_colors[i] = list(map(int, input().split()))


# 집의 도색 조건
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
def check_color(colors):
    # 비용 저장 List
    # 다음 index를 비교하기 위한 index 저장 용 list
    """
    1. 비용이 가장 낮은 색을 입력
    - min(colors)
    2. 해당 색에 대한 index 값 구하기
    - index = list.index(min(colors))
    3. 첫 번째 제한 조건 적용
    - 첫 번째 색을 제외하고 최솟값의 색을 적용
    4. 각 집은 전 후의 색이 다 달라야 한다.
    - 이전 index(0~2)를 다음 항목에서 제거 후 최솟값 구하기
    """
    total_costs = 0
    index_list = []
    for i, color_list in enumerate(colors):
        if len(index_list) > 0:
            color_list.pop(index_list[i - 1])
            color_list.insert(index_list[i - 1], 10000)
        total_costs += min(color_list)
        index_list.append(color_list.index(min(color_list)))
    return total_costs


print(check_color(homes_colors))


# -----------------정답-----------------


import sys

input = sys.stdin.readline
n = int(input())
rgb = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]  # 0으로 초기화
dp[0] = rgb[0]
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]  # 삘간색 0
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]  # 초록색 1
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]  # 파란색 2
print(min(dp[-1]))
