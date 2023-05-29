N = 987

def solution(n):
    digits = list(map(int, str(n)))

    return sum(digits)

print(solution(N))