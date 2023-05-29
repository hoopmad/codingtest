n = 300

def solution(n):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)

    return sum(factors)

# filter, lambda 사용
def sumDivisor(num):
    return sum(filter(lambda x: num % x == 0, range(1, num + 1)))

print(sumDivisor(n))