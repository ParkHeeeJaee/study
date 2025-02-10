import sys
# # # '''
# # 3
# # 1 2 3
# # 4 5 6
# # 7 8 9
# # '''
# # # 배열의 크기
# # N = int(input())
# # #
# # arr = [list(map(int, input().split())) for _ in range(N)]
# #
# # print(arr)
# #
#
# arr2 = [[0] * 4 for _ in range(3)]
# print(arr2)
#
# 부분집합의 합 문제 구현하기
# sys.stdin = open("input.txt","r")
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = 10
#
#     count_0 = 0
#
#     number_set = list(map(int, input().split()))
#
#     #원소의 개수가 N개인 집합의 부분집합 개수는 2^N(1<<N)
#     # 모든 부분집합을 보고 합이 0인지 확인하자
#     # 반복문 2^N 번
#     for i in range(1<<N):
#         # 1번 부분집합의 합이 0인지 확인
#         ith_subset_sum = 0
#         ith_subset = []
#
#         # i를 이진수로 바꿔서 생각해보자.
#         # 이진수의 각 자릿수는 0 또는 1
#         # 1인경우 그 인덱스에 있는 우너소를 부분집합에 포함
#         # 0인 경우 그 인덱스에 있는 원소를 부분집합에 포함하지 않음
#
#         # 각 자릿수에 1이 있는지 없는지 어떻게 아나??
#         # 이진수 1을 왼쪽으로 최대 N-1번 밀어 보면서 확인
#         # 왼쪽으로 0,1,2,3... N-1번 밀어가면서 확인
#         # 각 자릿수에 1이 있는지 없는지
#         for j in range(N):
#             # j : 왼쪽으로 밀어낸 횟수
#             if j & (1 << j):
#                     # 1을 이진수로 보고 j번째 비트에 1이 있다.
#                     # j번 인덱스에 있는 원소를 부분집합에 포함한 것으로 생각
#                     # i번 부분집합에는 j번 인덱스의 원소가 포함되어 있다
#                     ith-ith_subset_sum += number_set[j]
#                     ith_subset.append(number_set[j])
#
#             if ith_subset_sum == 0:
#                 count_0 = 1
#                 print(ith_subset)
#     print(f'f{tc} {count_0}')


# 2일차 - 색칠하기
# T = int(input())
# for tc in range(1, T + 1):
#
#     grid = [[0] * 10 for _ in range(10)]
#
#     N = int(input()) # 다음 줄부터 테스트 케이스의 첫 줄에 칠할 영역의 개수
#     # N개 색칠
#     for _ in range(N):
#         # 시작점, 끝점, 색
#         r1, c1, r2, c2, color = map(int, input().split())
#         new_color = 0
#         # 영역 구하기 (2차원 리스트로 생각)
#         for i in range(r1, r2 +1):
#             for j in range(c1, c2 + 1):
#                 if grid[i][j] == 0:
#                     grid[i][j] = color
#                 if grid[i][j] != color:
#                     grid[i][j] = 3 # 보라색 색 3으로 저장
#
#     result = 0
#     for i in range(10):
#         for j in range(10):
#             if grid[i][j] == 3:
#                 result += 1
#     print(f'#{tc} {result}')

# 2일차 부분집합의 합
T = int(input())

for tc in range(1, T + 1):

    N, K = map(int, input().split())
    A = list(range(1, 13)) # 전체 - N
    Count_K = 0
    A_len = len(A)

    for i in A(N, K):
        if A[i : i+N] == K:
            Count_K += 1
        # if A[i : i+N] != K:
        #     Count_K = 0

    print(f'#{tc} {count_K}')