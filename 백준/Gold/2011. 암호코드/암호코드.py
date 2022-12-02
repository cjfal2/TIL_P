N = '0' + input()

if N[1] == '0': # 인풋의 첫 번째가 0이면 무조건 컷
    print(0)
    quit()

memo = [1] + [0 for _ in range(len(N)-1)]
# 인풋의 길이가 1일 경우 if를 통과했다면 반드시 경우의 수가 1개이므로 맨 앞을 1로 지정
# 1로 지정을 해줬으니 range의 길이를 1을 빼줌
for i in range(1, len(N)):
    # print("=========", N[i],"==========")
    # N[i] 번째에 대해서 계산할 것임
    if int(N[i]) > 0:
        # N[i]가 양의 정수이면 앞에 저장한 memoization을 이용
        memo[i] += memo[i-1]

    # N[i-1] 과 N[i] 가 붙어 있는 경우에 대해서도 계산해봄
    # N[i-1]이 0이면 자동으로 컷 당함
    if 10 <= int(N[i-1] + N[i]) < 27:
        # memo[i-2]를 더하는 이유는 N[i-1]을 이용해서 경우의 수를 계산했기 때문
        # if else로 걸지 않고 i번째 인풋 수의 경우의 수를 모두 더해 나감
        memo[i] += memo[i-2]
# 마지막에 있는 메모이제이션을 출력
print(memo[-1]%1000000)