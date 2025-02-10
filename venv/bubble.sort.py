# lst = [55, 7, 78, 12, 42]
#
#
# def bubble_sort(lst):
#     n = len(lst)
#     # numbers : 정렬하고 싶은 배열(리스트)
#     #
#
#     # i번 인덱스의 자리 주인 정하기(n-1 ~ 1)
#     for i in range(n - 1):
#         # 앞에서부터 두개씩 비교, 큰게 뒤로 가도록 자리 바꾸기
#         for j in range(n - 1 - 1):
#             if lst[j] > lst[j + i]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#
#             print(lst)
#
#
# sorted_arr = bubble_sort(lst)
# print("\n✅ 정렬 완료:", sorted_arr)

# 실습
lst = [55, 7, 78, 12, 42]
def bubble_sort(a, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

a_lst = bubble_sort(lst, len(lst))
print (a_lst)