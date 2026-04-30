def solution(n):
    prime_number = [True] * (n + 1)
    
    for i in range(2, n + 1):
        for j in range(i * i, n + 1, i):
            prime_number[j] = False
    
    return sum(prime_number[2:])