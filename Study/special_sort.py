# T = int(input())
#
# N = int(input())
#
# # 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수
# # 큰 수와 작은 수를 번갈아 정렬
# # 1. i , # ex) N = 10, 10 1 9 2 8 3 7 6 5
#
# # N - i - 1 = n - i - 1,i 순으로 집어넣기 -> i = 10, 10 1, i = 인덱스 번호
#
# def special_sort(lst, N):
#     # 가장 큰 수 찾기? or 큰 수부터 정렬한 후 위 방법으로 사이에 정수 넣기?
#
#     for i in range(N-1):
#         # i번 자리의 주인을 찾는다.
#         # 남은 원소들 중에서 제일 작은 원소(오른쪽에서 찾기)
#
#         max_idx = i # 제일 작은 원소의 인덱스
#
#         # i 오른쪽에 있는 숫자들 중에 최솟값 찾기
#         for j in range(i +1, N):
#             # i + 1 부터 제일 작은 원소 찾기 시작
#             if lst[max_idx] > lst[j]:
#                 # min_idx 에 있던 원소보다 현재 j에 있는 원소가 더 작으면 갱신
#                 max_idx = j
#
#         # 찾은 최솟값의 인덱스를 사용해서 자리 바꿔주기
#         lst[i], lst[max_idx] = lst[max_idx], lst[i]
#
#
#
#
# for tc in range(1, T + 1):
#     print(f'{tc} {special_sort}')

def special_sort_selection(lst, N):
    """
    선택 정렬을 활용하여 큰 수 - 작은 수 순서로 정렬하는 함수
    """
    for i in range(N // 2):  # 절반만 반복 (큰 수 - 작은 수 번갈아 정렬)
        # 최댓값 찾기
        max_idx = i
        for j in range(i, N):
            if lst[j] > lst[max_idx]:
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]  # 최댓값을 앞쪽으로 이동

        # 최솟값 찾기 (최댓값을 찾은 후 다음 번 자리에서)
        min_idx = N - 1 - i
        for j in range(i + 1, N):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[N - 1 - i], lst[min_idx] = lst[min_idx], lst[N - 1 - i]  # 최솟값을 뒷쪽으로 이동

    return lst
print(special_sort_selection())
