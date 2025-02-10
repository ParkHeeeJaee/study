DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)

Counts = [0] * 5

Temp = [0] * N

for i in range(N):
    Counts[DATA[i]] += 1

print(Counts)

for i in range(1, 5):
    Counts[i] += Counts[i - 1]

print(Counts)
#
# for i in range(N-1, -1, -1):
#     Counts[DATA[i] -= 1


# arr = [2, 3, 7]
# for i1 in range(0, 3):
#     for i2 in range(0, 3):
#         if i1 != i2:
#             for i3 in range(0, 3):
#                 if i1 != i3 and i2 != i3:
#                     print(arr[i1], arr[i2], arr[i3])