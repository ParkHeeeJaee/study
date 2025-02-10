# sum

# 구해야 할 것 : 행의 합, 열의 합, 대각선의 합 중 최댓값
def max_sum_grid (tc, grid):
    # 대각선의 합 (오른쪽, 왼쪽) [i][i] <- 왼쪽에서 아래로, [i][100-i]
    sum_l_di = 0
    sum_r_di =  0
    max_sum_r_c = 0 # ??
    n = 100 # 인덱스 0 ~ 99 까지
    for i in range(n):
        sum_row = sum(grid[i])    #행의 합 = 그냥 한줄 arr[i]
        sum_col = sum(grid[j][i] for j in range(n))     # 열의 합 세로 한 줄 arr[j][i] -> for 문 돌려서 j 돌리기
        sum_l_di += grid[i][i]
        sum_r_di += grid[i][n - 1 - i]

        max_sum_r_c = max(sum_row, sum_col)

    max_sum_all = max(max_sum_r_c, sum_l_di, sum_r_di)
    return max_sum_all


for _ in range(10):
    tc = int(input().strip())
    # 리스트 배열이라 100 * 100 하면 나만 힘듬.
    grid = [list(map(int, input().split())) for _ in range(100)]
    result = max_sum_grid(tc, grid)
    print(f'#{tc} {result}')