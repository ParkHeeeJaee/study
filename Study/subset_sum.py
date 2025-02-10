T = int(input())

def count_subset(N, K):
    # 1~ 12까지의 수 1 ~ 12+1
    num_lst = list(range(1, 13))
    count = 0
    for i in range(1 << 12): # 부분 집합의 개수 2n개
        subset = []
        for j in range(12): # 0~11 까지. 인덱스 번호임
            if i & (1 << j): # j 번째 원소 확인
                subset.append(num_lst[j])
                # N개의 원소를 가진 부분집합 == 원소의 합이 K 인것 확인 후 카운트 +
        if len(subset) == N and sum(subset) == K:
            count += 1
    return count


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = count_subset(N, K)
    print(f'#{tc} {result}')
