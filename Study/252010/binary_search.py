# # def binary_search(a, n, key):
# #     # 검색구간 설정
# #     start = 0
# #     end = n-1
# #     while start <= end: # 검색 구간의 1개 이상의 원소가 있으면 검색을 실행해라
# #         middle = (start + end) // 2 # 기준 위치 개산
# #         if a[middle] == key:
# #             return middle
# #         elif a[middle] > key:
# #             end = middle - 1
# #         else:
# #             start = middle + 1 # a[middle] < key, 키보다 작으면 오른쪽 구간
# #     return -1 # 검색구간이 남아있지 않으면, 검색 실패
# #
# # arr = [2, 4, 7, 9, 11, 19, 23]
# #
# # print(binary_search(arr, len(arr), 19))
# # print(binary_search(arr, len(arr), 100))
# # print(binary_search(arr, len(arr), 1))
#
# # 오프라인 코칭
# def binary_search(lst, N, key):
#     # lst : 검색 대상 리스트
#     # N : 검색 대상 리스트의 길이
#     # key : 내가 찾는 값(목표 값)
#
#     # 내가 찾는 값을 어디서 찾을지?
#     # 그 범위를 계속 반씩 줄여 나감
#     # 내가 인덱스 범위를 저장하는 변수를 직접 조정
#     start = 0 # 검색 시작 위치(인덱스)
#     end = N -1 # 검색 마지막 위치(인덱스)
#     # 값을 검색 반복, 반복횟수가 정해져 있지 않기 때문에 while 사용
#     # start 와 end가 정상 범위를 나타내면 반복
#     while start <= end:
#         # start 가 end 이하이면 제대로된 범위
#         # start와 end가 교차 되버리면 잘못된 범위
#
#         # 일단 가운대 찍어
#         mid = (start + end) // 2
#
#         print (start, end)
#
#         if lst[mid] == key:
#             # 아이갓츄
#             # 찾은 값의 위치 인덱스 반환
#             return mid
#         elif lst[mid] > key:
#             # 아이갓츄 실패, 이 값이 내가 원하는 값보다 크다 ex) ~[mid] = 50, ~[key] = 30 왼쪽으로 가야함
#             end = mid -1
#         else:
#             # 아이갓츄 실패 이번엔 오른쪽 으로 감 start지점을 옮김.
#             start = mid + 1
#
#     # 반복문이 종료 start > end 인 상황
#     return -1
#
# numbers = [2, 3, 5, 7, 8, 9, 11]
#
# print(binary_search(numbers, len(numbers), 11))
# print(binary_search(numbers, len(numbers), 111))

# 실습 이진 탐색

def game(p, target):
    start = 1
    end = p
    # book = []
    count = 0
    while start <= end:
        middle = int((1+end)//2)
        count += 1
        if middle == target:
            return count
        elif middle > target:
            end = middle - 1
        else:
            start = middle + 1

    return count

T = int(input())
for tc in range(T, T + 1):
    p, pa, pb = map(int, input().split())

    # if game(p, pa) == game(p, pb):
    #     print(f'{tc} {0}')
    count_a = game(p, pa)
    count_b = game(p, pb)

    if count_a == count_b:
        print(f'#{tc} 0')
    elif count_a < count_b:
        print(f'#{tc} A')
    else:
        print(f'#{tc} B')
    # winner = min(game(p, pa), game(p, pb))
    # print(f'{tc} {winner}')

#
# start = 1
# end = 400-1
# while start <= end: # 검색 구간의 1개 이상의 원소가 있으면 검색을 실행해라
#     middle = (start + end) // 2 # 기준 위치 개산
#     if a[middle] == key:
#         return middle
#     elif a[middle] > key:
#         end = middle - 1
#     else:
#         start = middle + 1 # a[middle] < key, 키보다 작으면 오른쪽 구간
# return -1 # 검색구간이 남아있지 않으면, 검색 실패