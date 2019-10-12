# 홀수 1 3 5 7 9를 반복문으로 출력 하는 함수를
# 1부터 91까지 모든 홀수를 출력 해보세요
# 만들어 보세요
# 등차수열
# 1 3 5 7 9 -> 2씩 차이남
# 2 4 6 8 10 -> 2씩 차이남
# 2n
# 2n + 1 (0 <= n)
# 2num - 1 (1 <= num)
def printOdds():
    for num in range(0, 5):
        print(2 * num + 1)
printOdds()