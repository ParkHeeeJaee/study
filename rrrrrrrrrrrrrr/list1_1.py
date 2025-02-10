'''
6
2 7 5 3 1 4
'''
# N = int(input())
# arr = list(map(int, input().split()))
#
# #배열원소의 합 s 구하기
# s = 0
# for i in range(N):
#     s += arr[i]
#
# print(s)
#
# #최대값 찾기
# def my_max(arr,N):
#     max_val = arr[0]
#     for i in N:
#         if max_val < arr[i]:
#             max_val = arr[i]
#
# # 최대값 찾기 최소값 찾기
# def Max_Min(arr, N):
#     max_val = arr[0]
#     for i in range(N):
#         if max_val < arr[i]:
#             max_val = arr[i]
#
#     min_val = arr[0]
#     for i in range(N):
#         if min_val > arr[i]:  # 최솟값 찾기 (부등호 수정)
#             min_val = arr[i]
#
#     return max_val - min_val  # return을 반복문 밖으로 이동


# 입력 받기
N = int(input())  # 정수 입력
arr = list(map(int, input().split()))  # 리스트 입력

# 배열 원소의 합 s 구하기
s = 0
for i in range(N):
    s += arr[i]
print(s)


최대값 찾기
def my_max(arr, N):
    max_val = arr[0]
    for i in range(N):
        if max_val < arr[i]:
            max_val = arr[i]
    return max_val  # return 추가


# 최대값 - 최소값 찾기
def Max_Min(arr, N):
    max_val = arr[0]
    for i in range(N):
        if max_val < arr[i]:
            max_val = arr[i]

    min_val = arr[0]
    for i in range(N):
        if min_val > arr[i]:  # 최솟값 찾기
            min_val = arr[i]

    return max_val - min_val  # return을 반복문 밖으로 이동


# 함수 호출 및 결과 출력
result = Max_Min(arr, N)
print(result)

#
# #최대값 인덱스 찾기

# def w_my_max(arr,n):
#     max_idx = 0
#     for i in range(1, N):
#         if arr[max_idx] < arr[i]:
#             max_idx = i

# T = int(input()) #테스트케이스 개수
# for tc in range(1, T+1): # 케이스별로 처리
#     N = int(input()) #케이스 별 입력 개수
#     arr = list(map(int, input().split()))
#
#     max_v = arr[0] # 첫 원소를 최대값으로 가정
#     min_v = arr[0] # 첫 원소를 최솟값으로 가정
#
#     #최대,최소 코드
#     for i in range(1, N):
#         if max_v < arr[i]:
#             max_v = arr[i]
#         if min_v > arr[i]:
#             min_v = arr[i]
#
#     print(f'#{tc} {max_v - min_v}')
# ```
# 5
# 10 20 30 40 50
# ```
#
# n = int(input())
# lst = list(map(int, input(),split()))