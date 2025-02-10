# # # #
# # #
# def selection_sort(a, n):
#     for i in range(n-1): # 기준위치(최솟값을 찾는 구간의 시작)
#         min_idx = i # 최솟값 인덱스 초기화, 구간의 맨 앞 원소를 최소로 가정
#         for j in range(i+ 1, n): # 실제 최솟값인지
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
# # #
# # #
# # #
# # # arr= [10 ,25, 64, 22, 11]
# # # selection_sort(arr, len(arr))
# # # print(arr)
# #
# # 오프라인 코칭
# def selection_sort(lst, N):
#     # lst : 정렬 대상
#     # N : 리스트 길이(배열 길이)
#
#     # 오름차순으로 정렬한다고 했을 때
#     # 맨 앞자리부터 자리의 주인을 정한다.
#     # 자리의 주인은 최소값으로 선택
#     # 0번자리 : 최솟값 1번자리 그다음 최소.... n-1번 자리 = 최댓값, n-2까지 해도 N-1번 자리는 확정
#     for i in range(N-1):
#         # i번 자리의 주인을 찾는다.
#         # 남은 원소들 중에서 제일 작은 원소(오른쪽에서 찾기)
#
#         min_idx = i # 제일 작은 원소의 인덱스
#
#         # i 오른쪽에 있는 숫자들 중에 최솟값 찾기
#         for j in range(i +1, N):
#             # i + 1 부터 제일 작은 원소 찾기 시작
#             if lst[min_idx] > lst[j]:
#                 # min_idx 에 있던 원소보다 현재 j에 있는 원소가 더 작으면 갱신
#                 min_idx = j
#
#         # 찾은 최솟값의 인덱스를 사용해서 자리 바꿔주기
#         lst[i], lst[min_idx] = lst[min_idx], lst[i]
#
#
# lst = [5, 1, 2, 9, 4, 3]
# selection_sort(lst, len(lst))
# print(lst)

# def special_selection(lst, N):
#     sorted_result = []
#     lst.sort(reverse=True)  # 내림차순 정렬
#
# # lst를 내림차순 정렬한 후 i -> N - 1 - i 출력을 반복 ex) N = 10, 10 1 9 2 ...
#     for i in range(N // 2):
#         sorted_result.append(lst[i])
#         sorted_result.append(lst[N - 1 - i])
#
# # 이렇게 하면 마지막 10번 째 원소가 빠짐. 따로 추가해줘야함.
#     if N % 2 == 1:
#         sorted_result.append(lst[N // 2])
#
#     return sorted_result
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     print(lst)
#     print(f'#{tc} {special_selection(lst, N)}')


###
# def special_selection(lst, N):
#     sorted_result = []
#     lst.sort(reverse=True)  # 내림차순 정렬
#
#     for i in range(N // 2):
#         sorted_result.append(lst[i])
#         sorted_result.append(lst[N - 1 - i])
#
#     if N % 2 == 1:
#         sorted_result.append(lst[N // 2])
#
#     return sorted_result
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#
#     result = special_selection(lst, N)
#
#     # 리스트를 문자열로 변환해서 출력
#     print(f'#{tc} {" ".join(map(str, result))}')
#

###
# 가장 큰 수 먼저 찾기?
# 정렬하는 방법? max_lst = lst[N-1-i], lst[i] append 로 올리고, 계속 진행?
# 그 다음 조건?
#
# or 정렬 후 홀수 짝수 나누어서 인덱스 추가? N = 10 ,20 홀수 짝수인 경우 있어서 모르겠음.
#
# def selection_sort(a, n):
#     for i in range(n-1):
#         max_idx = i
#         for j in range(i+ 1, n):
#             if a[max_idx] < a[j]:
#                 max_idx = j
#         a[i], a[max_idx] = a[max_idx], a[i]
#  # 정렬  된 값 (내림차순)
#     for i in range(n-1):
#
#
#
# ###
# def  special_sort(N, ai):
#     for i in range(N-1):
#         max_idx = i
#         for j in range(N-1):
#             if list
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     ai = list(map(int, input().split()))
#
#     result = specail_sort(N, ai)
#     print(f'#{tc} {result}')
#
#     ###
#
#     T = int(input())
#     for tc in range(1, T + 1):
#         N = int(input())
#         arr = list(map(int, input().split()))
#
#         for i in range(N - 1):
#             min_idx = i  # 첫번째 숫자 최솟값 지정
#             for j in range(i + 1, N):
#                 if arr[min_idx] > arr[j]:
#                     min_idx = j  # 최솟값 변경
#             arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
#         print(f"#{tc}", end='')
#         for i in range(5):
#             print(f" {arr[N - i - 1]} {arr[i]}", end='')
#         print()

###
# 리스트의 인덱스가 짝수/홀수인 경우에
# 각각 최대/최소를 고르는 선택정렬
# *** 출력 10개까지만 ***


# def special_sort(a, n):
#     for i in range(n - 1):
#         if i % 2 == 0:
#             max_idx = i
#             for j in range(i, n):
#                 if a[max_idx] < a[j]:
#                     a[max_idx], a[j] = a[j], a[max_idx]
#         else:
#             min_idx = i
#             for j in range(i, n):
#                 if a[min_idx] > a[j]:
#                     a[min_idx], a[j] = a[j], a[min_idx]
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     special_sort(numbers, N)
#
#     print(f"#{tc}", end=" ")
#     for i in range(10):
#         print(num)

def special_sort(a, n): # 선택정렬 활용
    for i in range(n -1):
        if i % 2 == 0:
            max_idx = i
            # 가장 큰 값을 찾은 후 i에 할당 할 것.
            for j in range(i, n):
                if a[max_idx] < a[j]:
                    a[max_idx], a[j] = a[j], a[max_idx]
                    # i 번째 인덱스에 최댓값 할당 됨. 이후 i 번째 이후를 순회함으로 순차적으로 쌓임.
        else:
            min_idx = i
            for j in range(i, n):
                if a[min_idx] > a[j]:
                    a[min_idx], a[j] = a[j], a[min_idx]

    return a


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ai = list(map(int, input().split()))
    result = special_sort(ai, n)
    print(f'#{tc}', *result[:10])
