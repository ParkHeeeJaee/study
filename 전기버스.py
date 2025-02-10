def drive(K, N):
    # 버스를 운행하는 함수
    # return 0 : 충전소가 제대로 배치되어 있지 않다
    # retunr 한 값>0 : 충전소가 제대로 배치되어 있다.
    
    count = 0 #지금까지 충전한 횟수
    current = K # 현재 위치,버스가 한번 충전해서 최대로 이동한 상태
    last = 0 # 마지막으로 충전한 위치
    while current < N:
        # 현재 정류장에 충전긱 있나 없나 검사
        # 충전기가 만약 없다면 충전기를 찾아서 다시 뒤로 한칸씩 이동
        # 충전기를 찾을 때 까지
        while stop[current] == 0:
            # current 정류장에 충전기가 없다면 뒤로 한칸 이동
            current -= 1 # 한칸씩 뒤로 이동
            # 마지막으로 충전한 정류소 까지 가면, 끝까지 갈 수 없음.
            if current == last:
                return  0 # 운행불가, 함수 종료

        # 만약 반복문이 중단되서 코드가 역기까지 실행된다면
        # 충전기가 있는 정류소에 도착했다.
        # 마지막으로 충전한 정류소 번호 기억
        last = current
        # 다음 위치로 이동
        current += K
        # 충전 횟수 + 1
        count += 1

    #
    #
    #
    return count





T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K : 이동할 수 있는 정류장 개수
    # N : 총 정류장 개수
    # M : 충전기 개수
    charger = list(map(int,input().split()))
    # 충전이 가능한 정류장인가? 불가능한 정류장인가?
    stop = [0] * N
    # stop[i] == 1 : i번 정류장에는 충전기가 있다!
    # stop[i] == 0 : i번 정류장에는 충전기가 없다!
    # if stop[i] == 1 :
    # 충전해라
    for i in charger:
        #i번 정류장에는 충전기가 있어요 표시
        stop[i] = 1

    answer = drive(K, N)
    print (f'#{tc} {answer}')