'''
아래 방향으로 진행, 좌우 방향 이동 가능 시 이동 가능.
바닥에 도착하면 멈춤.
100 * 100 크기의 2차원 배열, 도착점에 대응되는 출발점 x 반환하는 코드 작성
0으로 채워진 평면, 사다리는 연속된 1, 도착지점 2
다른 막대 가로지르기 x

'''

for tc in range(1, 11):
    T = int(input()) #?? for 문 밖에 있는 T를 안으로 넣었더니 문제가 해결됨.
    # 총 배열. 2차원 리스트 100 * 100
    grid = [list(map(int, input().split())) for _ in range(100)]
    # grid = [list(map(int, sys.stdin.readline().split())) for _ in range(100)]
    # 도착 지점 2 = 마지막 행에서 값이 2인곳
    for x in range(100):
        if grid[99][x] == 2: # <- y = 행, x = 열
            start_point = x # 도착 지점의 x 좌표
            break # 2를 찾았으니 for문 종료. 2는 하나만 존재함.

    # 도착 지점 찾았으니 다시 위로 올라가기.
    # 도착 지점에서 시작

    y, x = 99, start_point

    while y > 0: # 0에 닿을 때 까지 확인
        if x > 0 and grid[y][x - 1] == 1: #왼쪽이 1 이라면 이동 가능.
            while x > 0 and grid[y][x - 1] == 1: # 왼쪽에 1이 있으면 계속 이동
                x -= 1 # 왼쪽으로 한 칸 이동

        elif x < 99 and grid[y][x + 1] == 1:
            while x < 99 and grid[y][x +1] == 1: # 오른쪽에 1이 있으면 계속 이동
                x += 1 # 오른쪽으로 한칸 이동

        y -= 1 # 위로 한칸 이동


    print(f'#{tc} {x}') # 출발 위치