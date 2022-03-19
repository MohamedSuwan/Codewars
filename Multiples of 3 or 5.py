def solution(n):
    return sum(i for i in range(n) if i%5==0 or i%3==0)
