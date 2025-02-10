#
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
#
#
# [입력]
#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
#
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
#
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#
# T = 3
# N = 5
# ai = [477162, 658880, 751280, 927930, 297191]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


# T = int(input())
#
# def max_min_val(N,ai):
#     max_val = ai[0]
#     min_val = ai[0]
#
#     for i in ai:
#         if i > max_val:
#             max_val = i
#         if i < min_val:
#             min_val = i
#
#     return max_val - min_val
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     ai = list(map(int, input().split()))
#     result = max_min_val(N,ai)
#
#     print (f'#{test_case} {result}')

# 구간합
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# def sum_num(n, m, ai):
#     arr = ai[:]
#     max_sum_num = 0
#     min_sum_num = 0
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#     for i in range(m):
#         min_sum_num += arr[i]
#
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if arr[j] < arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     for i in range(m):
#         max_sum_num += arr[i]
#
#     return max_sum_num - min_sum_num
#
# for test_case in range(1, T + 1):
#
#     NM = list(map(int, input().split()))
#     ai = list(map(int, input().split()))
#     n = NM[0]
#     m = NM[1]
#
#     result = sum_num(n, m, ai)
#     print(f'#{test_case} {result}')

#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     ai = list(map(int, input().split()))
#     max_val = sum(ai[:M])
#     min_val = sum(ai[:M])
#     for i in range(N-M+1):
#         max_val = max(max_val, sum(ai[i:i+M]))
#         min_val = min(min_val, sum(ai[i:i+M]))
#
#     result = max_val - min_val
#     print(f'#{test_case} {result}')

# 조망권이 확보된 세대의 수
# 양 옆 빌딩 사이의 거리
# list[0] 과 list[N-1] 건물은 각각 좌, 우 건물을 생각하지 않아도 됨
# n 개의 건물과, n개 건물의 높이,
# 현재 건물을 i 로 주고 for 문으로 순회
# 현재 건물 기준 i-2,i-1(왼쪽), i+1,i+2(오른쪽)





T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    high_arr = list(map(int, input().split()))
    # 각 건물의 높이
    for i in range(2, N-2):
        max_high_l = max(high_arr[i-2], high_arr[i-1])
        max_high_r = max(high_arr[i+1], high_arr[i+2])
        if