def counting_sort(DATA, TEMP, K):
    # DATA : 정렬 대상(배열)
    # TEMP : 정렬 결과(배열)
    # K : 정렬 대상 중 최댓값 == 카운트 배열의 크기

    Count = [0] * (K+1)
    # Count 카운트 배열(원소의 등장 횟수 세기)
    # C[x] : x의 등장 횟수
    # C[i] : DATA 안에 1이 몇개 있는가?

    for num in DATA:
        # DATA 배열 안에서 꺼내온 숫자 num의 등장 횟수 +1
        Count[num] += 1

    # 2. 각원소의 등장 횟수를 계산
    # 각 원소가 들어갈 자리 위치를 계산
    # 어떤 숫자 이하의 숫자가 몇개인지 안다면
    # 그 숫자의 위치를 알 수 있음.
    for i in range(1,len(Count)):
        Count[i] = Count[i] + Count[i-1]

    # 3. 뒤에서부터 DATA를 확인하면 서 Count 배열을 보고
    # 자리 확인, 정렬 Count 배열에 원소 - 1
    # DATA에서 숫자 X가 나왔다
    # Count[x] 에서 값 확인하고 -1 한 위치에 x를 넣는다.
    # 뒤에서부터 확인하는 이유는 안정 정렬(원래 순서 보장)
    for i in range(len(DATA) -1, -1, -1):
        # 자리에 놓기 전에 -1 잊지 말기
        # DATA[i] 이 원소의 위치는 ??
        Count[DATA[i]] -= 1

        #정렬 결과 배열 TEMP에 DATA[i] 놓기
        # DATA[i] : 정렬할 대상 원소 하나
        # Count{DATA[i]] : DATA[i]가 들어갈 인덱스 위치
        TEMP[Count[DATA[i]]] = DATA[i]

nums = [ 0, 4, 1, 3, 1, 2, 4, 1]
result = [0] * len(nums)
counting_sort(nums, result, max(nums))
print(result)