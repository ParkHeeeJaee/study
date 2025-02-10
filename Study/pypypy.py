# T = int(input())
#
# for test_case in range(1, T + 1):
#     dumps = int(input())
#     boxes = list(map(int, input().split()))
#
#     # 작업 횟수 만큼 반복하자.
#     for _ in range(dumps):
#         # 가장 높은 상자의 위치와
#         # 가장 낮은 상자의 위치를 구하고 싶다.
#         max_height = boxes[0]
#         max_idx = 0
#         min_height = boxes[0]
#         min_idx = 0
#         w = len(boxes) # w = 100으로 설정시 문제 발생
#
#         # 모든 상자를 확인하면서
#         # 가장 높았던 상자보다 높다면 갱신
#         # 가장 낮았던 상자보다 낮다면 갱신
#         for i in range(w):
#             if boxes[i] > max_height:
#                 max_height = boxes[i]
#                 max_idx = i
#             if boxes[i] < min_height:
#                 min_height = boxes[i]
#                 min_idx = i
#
#         # 어디에 제일 큰지, 작은지 알았음
#         # 평탄화
#         boxes[max_idx] -= 1
#         boxes[min_idx] += 1
#
#     # 최종 최대값과 최소값을 구한 후 출력
#     max_height = max(boxes)
#     min_height = min(boxes)
#     print(f'#{test_case} {max_height - min_height}')

T = int(input().strip())
for test_case in range(1, T + 1):
    # cards = list(map(int, input().split()))
    # 불가능 map 함수의 작동방식과 연관 iterable 한 요소가 아님.
    # input 은 문자열로 받음, split 공백 문자 기준으로 자르려고 시도. 공백 없음.
    card = int(input().strip())
    cards = list(map(int, input().strip()))

        # 카드는 0~9까지임.
        # 0 ~ 9 (10개) 리스트로 각 카드가 등장한 횟수 카운트
    counts = [0] * 10

        #각 카드를 확인. 카드에 적혀있는 숫자의 count를 증가
    for card in cards:
        # 카드에 적힌 숫자의 count 리스트를 하나 증가
        counts[card] += 1

    max_count = 0
    max_card = 0
        # 각 카드의 등장 기록인 (counts)를 순서대로 확인.
    for i in range(10):
        # 그 중 (counts[i])가 가장 높은 카드를 찾음.
        if counts[i] >= max_count:
            max_card = i
            max_count = counts[i]

    print(f'#{test_case} {max_card} {max_count}')

# # 정수 N 개, 구간의 개수
# N, M = list(map(int, input().split()))
# for i in range(M):
#     max_sum += nums[i]
#     min_sum += nums[i]
#
# # 다음 순번에서는 range를 어떻게 써야할까?
# for i in range(1, M+1):
#
# # 그 다음 순번은?
# for i in range(2, m+2):

