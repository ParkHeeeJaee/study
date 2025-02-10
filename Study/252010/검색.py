# def seq_search(a, n, key):
#     for i in range(n):
#         if a[i] == key:
#             return i
#     return -1
#
# arr = [4, 9, 11, 23 , 2, 19, 7]
# print(seq_search(arr, len(arr), 8))
#
# arr = [4, 9, 11, 23 , 2, 19, 7]
# key = 11
# ans = -1
# for i in range(arr, key):
#     if arr[i] == key:
#         ans = i
# print(arr)



# arr= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# N = 3
# key =5
# ans = 0 # key 가 있으면1, 없으면 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == key:
#             ans =1
#             break # for j를 빠져나옴( 이중 포문은 한번에 못 빠져나옴)

#
# arr= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# N = 3
# key = 5
#
# def seq_search(N, key):
#
#     ans = 0  # key 가 있으면1, 없으면 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == key:
#                 ans =1
#                 return 1
#     return 0
#
# print(seq_search(N, key))