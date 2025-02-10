# 0123(우하좌상)
# d = 0
# d== 4 -> 0

# d += 1 조건
# 1. 범위 벗어남 - > N 을 초과, N 은 점차 감소해야함 for 문을 통해 i 만큼 감소
# 2. 값이 있는곳

T = int(input())
def is_valid(r, c):
    return 0<= r < N and 0 <= c < N and snail[r][c]


for tc in range(1, T+1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]

    # 방향 우 하 좌 상 우 하 좌 상 ...
    d = 0
    # 0우 1하 2좌 3상
    dr = [0, 1, 0, -1] # 행
    dc = [1, 0, -1, 0] # 열

    # 집접 행 번호와 열 번호를 관리 해야함.
    # r : 행 번호, c : 열 번호

    for i in range(1, N * N +1):
        snalil[r][c] = 1

        nr = r + dr[d]

        nc = c + dc[d]

        # 다음 위치가 두 조건을 만족하면 그대로 계속
        #1. 2차원 배열 범위 안
        #2. 숫자를 쓴적이 없음(ㅇ)
        if is valid(nr, nc):
            r,c = nr, nc

        # 만약 아니라면 nr, nc는 다시 계산하여야 함.
        # 방향을 바꿔서 계산
        else:
            d + d(d+1) % 4
        #     d= d + 1 if d < 3 els
        # #     d = d + 1e 0
        #     if d > 3
        #     else:
        #          return 0
        r = r + dr[d]
        c = c + dc[d]

        print(f' #{tc}')
        for i in range(N):
            print(*sbauk[i]) # * 언패킹


# 내가 한것
# 1.
def generate_snail_matrix_fixed(N):
    snail = [[0] * N for _ in range(N)]

    # 방향: 우(0), 하(1), 좌(2), 상(3)
    dr = [0, 1, 0, -1]  # 행 변화
    dc = [1, 0, -1, 0]  # 열 변화

    r, c = 0, 0  # 시작 위치
    CN = N  # 이동 거리
    num = 1
    d = 0  # 방향 인덱스

    while CN > 0:
        for _ in range(CN):  # 현재 길이만큼 이동
            snail[r][c] = num
            num += 1

            # 다음 위치 이동 (마지막 이동 전까지만 이동)
            if _ < CN - 1:
                r += dr[d]
                c += dc[d]

        # 방향 전환
        d = (d + 1) % 4

        # 방향이 우(0) 또는 좌(2)일 때만 CN 감소 (한 사이클마다 2번 감소해야 함)
        if d == 1 or d == 3:
            CN -= 1

        # 새로운 방향에서 한 칸 이동
        r += dr[d]
        c += dc[d]

    return snail

# 결과 출력
results = {}
for i, N in enumerate(test_cases, start=1):
    results[f"Case #{i}"] = generate_snail_matrix_fixed(N)

#2.
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]

    # 방향 우 하 좌 상 우 하 좌 상 ...
    d = 0
    # 0우 1하 2좌 3상
    dr = [0, 1, 0, -1] # 행
    dc = [1, 0, -1, 0] # 열

    # 집접 행 번호와 열 번호를 관리 해야함.
    # r : 행 번호, c : 열 번호
    r, c = 0, 0
    CN = N
    num = 1
    # for i in range(1, N*N+1):
    #     # 리스트이기때문에 행과 열의 인덱스 번호가 N을 초과할 수 없음. CN에 N의 값을 할당 후 진행.
    #     # 우 / 좌 이후 CN -= 1
    #     if i > CN pass:
    #         CN -= 1

    while CN > 0:
        for _ in range(CN):  # 현재 길이만큼 이동
            snail[r][c] = num
            num += 1
            # 다음 위치 이동
            r += dr[d]
            c += dc[d]

        # 방향 전환
        d = (d + 1) % 4

        # 방향이 0(우) 또는 2(좌)일 때만 CN 감소
        if d == 0 or d == 2:
            CN -= 1

        # 출력
    print(f"#{tc}")
    for row in snail:
        print(*row)